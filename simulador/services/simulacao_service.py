from simulador.models import Simulacao
from datetime import date
from dataclasses import dataclass

@dataclass
class SimulacaoDTO:
    conta_nova: float
    economia_total: dict[str, float]
    quantidade_paineis: int
    maximo_paineis: int
    area_utilizada_m2: float
    porcentagem_area: float
    energia_gerada_kwh: float
    energia_consumida_kwh: float
    potencia_sistema_kwp: float
    total_investimento: float
    porcentagem_economia: float
    payback_meses: int
    uso_pratico: dict[str, int]

class SimulacaoService:
    _percentuais_tusd = {
        2023: 0.15,
        2024: 0.30,
        2025: 0.45,
        2026: 0.60,
        2027: 0.75
    }

    def __init__(self, simulacao: Simulacao):
        self.simulacao = simulacao

    @classmethod
    def obter_percentual_tusd(cls, ano: int) -> float:
        '''Função auxiliar para obter a porcentagem de cobrança do TUSD'''
        if ano >= 2028:
            return 1.0
        return cls._percentuais_tusd[ano]

    def calcular_tarifa_disponibilidade(self, potencia: float, te: float, tusd: float):
        '''Calcula o valor mínimo de cobrança pela concessionária de energia.'''
        potencia = abs(potencia)
        if potencia <= 8:
            kwh_minimo = 30
        elif potencia <= 50:
            kwh_minimo = 50
        else:
            kwh_minimo = 100
            
        return kwh_minimo * (te + tusd)
    
    def calcular_tarifas_adicionais(self, base_tributavel: float) -> float:
        ''' Calcula ICMS, PIS + COFINS e COSIP (Iluminação Pública)'''
        icms = 0.18 * base_tributavel
        pis_cofins = 0.095 * base_tributavel
        cosip = 20.0
        total = icms + pis_cofins + cosip
        return total

    def calcular_tarifa_liquida(self, consumo_rede: float, geracao_kit: float, potencia_kit: float):
        '''Função que calcula o valor líquido (compensação/injeção + taxas adicionais) sobre a energia de um kit de paineis solares.'''
        ano = int(date.today().strftime('%Y'))
        percentual_cobranca = self.obter_percentual_tusd(ano)
        tusd = self.simulacao.concessionaria.tusd
        te = self.simulacao.concessionaria.te

        # 1. Custo de Disponibilidade
        custo_disponibilidade = self.calcular_tarifa_disponibilidade(potencia_kit, te=te, tusd=tusd)

        # 2. Cálculo do Consumo Bruto
        energia_compensada: float = 0
        energia_injetada: float = 0
        valor_bruto: float
        if (geracao_kit < consumo_rede):
            energia_compensada = consumo_rede - geracao_kit
            valor_energia = energia_compensada * (tusd + te)
            valor_bruto = max(custo_disponibilidade, valor_energia)
        else:
            energia_injetada = geracao_kit - consumo_rede
            tusd_fio_b = energia_injetada * tusd * percentual_cobranca
            valor_bruto = custo_disponibilidade + tusd_fio_b
        
        # 3. Adição de Tarifas
        taxas = self.calcular_tarifas_adicionais(base_tributavel=valor_bruto)
        valor_liquido = valor_bruto + taxas

        return valor_liquido

    def calcular_economia(self, economia_mensal: float) -> dict[str, float]:
        economia_total = {
            '1_mes': economia_mensal,
            '5_meses': economia_mensal * 5,
            '1_ano': economia_mensal * 12,
            '3_anos': economia_mensal * 36,
            '5_anos': economia_mensal * 60,
            '10_anos': economia_mensal * 120 
        }
        return economia_total
    
    def calcular_uso_pratico(self, energia_mensal_kwh: float) -> dict[str, int]:
        potencia_lampada_w = 9
        horas_lampada_dia = 8
        dias_no_mes = 30
        consumo_lampada_kwh = (potencia_lampada_w * horas_lampada_dia * dias_no_mes) / 1000 

        geladeira_kwh_dia = 30
        maquina_lavar_kwh_ciclo = 0.75
        carro_eletrico_kwh_por_km = 0.15

        num_lampadas = energia_mensal_kwh / consumo_lampada_kwh # 8 horas por dia ligada
        num_geladeiras = energia_mensal_kwh / geladeira_kwh_dia # 24 horas por dia ligada
        num_lavagens = energia_mensal_kwh / maquina_lavar_kwh_ciclo # Consumo por ciclo
        autonomia_carro = energia_mensal_kwh / carro_eletrico_kwh_por_km # Quantos km vai rodar 

        return {
            'num_lampadas': int(num_lampadas),
            'num_geladeiras': int(num_geladeiras),
            'num_lavagens': int(num_lavagens),
            'autonomia_carro': int(autonomia_carro),
        }

    def calcular_viabilidade(self, perdas: float) -> SimulacaoDTO:
        '''Função que calcula a viabilidade da implementação de um determinado painel solar com base nos dados fornecidos pelo usuário (Simulacao). '''
        eficiencia_painel = self.simulacao.painel_solar.eficiencia / 100
        conta_luz_atual = self.simulacao.conta_luz      
        tarifa = self.simulacao.concessionaria.te + self.simulacao.concessionaria.tusd
        potencia_painel = self.simulacao.painel_solar.potencia
        area_disponivel = self.simulacao.area_disponivel
        valor_painel = self.simulacao.painel_solar.valor
        acrescimos = 2_000

        # 1. Obter HSP
        hsp_mensal = self.simulacao.endereco.hsp

        # 2. Obter Área do Painel
        area_painel = potencia_painel / (1000 * eficiencia_painel)

        # 3. Consumo Atual
        consumo_usuario = conta_luz_atual / tarifa

        # 3. Energia Gerada por Painel (kWh)
        energia_por_painel = (potencia_painel * hsp_mensal) / 1000 * (1 - perdas)

        # 4. Descobrir quantidade mínima de painéis
        energia_total = 0
        min_paineis = 0
        area_total = 0
        max_paineis = int(area_disponivel // area_painel)

        while (energia_total < consumo_usuario and min_paineis < max_paineis):
            energia_total += energia_por_painel
            area_total += area_painel
            min_paineis += 1
        
        qtd_paineis = min_paineis if (energia_total >= consumo_usuario) else max_paineis   
        porcentagem_area = area_total * 100 / area_disponivel
        
        # 5. Descobrir Informações de Economia
        area_total = area_painel * qtd_paineis
        potencia_total = qtd_paineis * potencia_painel / 1000
        total_investimento = valor_painel * qtd_paineis + acrescimos
        
        conta_final = self.calcular_tarifa_liquida(
            consumo_rede=consumo_usuario,
            geracao_kit=energia_total,
            potencia_kit=potencia_total
        )

        economia_mensal = conta_luz_atual - conta_final
        payback = total_investimento / economia_mensal
        economia_total = self.calcular_economia(economia_mensal)

        porcentagem_economia: float
        if (economia_mensal < conta_luz_atual):
            porcentagem_economia = (conta_luz_atual - conta_final) * 100 / conta_luz_atual
        else:
            porcentagem_economia = (conta_final - conta_luz_atual) * 100 / conta_final

        # 6. Descobrir informações ecológicas
        uso_pratico = self.calcular_uso_pratico(energia_total)
        
        return SimulacaoDTO(
            conta_nova=round(conta_final, 2),
            economia_total=economia_total,
            quantidade_paineis=int(qtd_paineis),
            maximo_paineis=int(max_paineis),
            area_utilizada_m2=round(area_total, 2),
            porcentagem_area=round(porcentagem_area, 2),
            energia_gerada_kwh=round(energia_total, 2),
            energia_consumida_kwh=round(consumo_usuario, 2),
            potencia_sistema_kwp=round(potencia_total, 2),
            total_investimento=round(total_investimento, 2),
            porcentagem_economia=round(porcentagem_economia, 2),
            payback_meses=int(payback),
            uso_pratico=uso_pratico
        )
        