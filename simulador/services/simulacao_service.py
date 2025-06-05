from simulador.models import Simulacao
from datetime import date
from simulador.dtos.simulacao_dtos import *
import math


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

    def calcular_acrescimos(self, valor_total: float) -> float:
        return valor_total * 1,65

    def calcular_tarifa_disponibilidade(self, potencia: float, te: float, tusd: float):
        '''Calcula o valor mínimo pelo consumo bifásico'''
        if potencia <= 12:
            kwh_minimo = 30
        elif potencia <= 25:
            kwh_minimo = 50
        else:
            kwh_minimo = 100
        return kwh_minimo * (te + tusd)
    
    def calcular_tarifas_adicionais(self, base_tributavel: float) -> TarifasAdicionaisDTO:
        ''' Calcula ICMS, PIS + COFINS e COSIP (Iluminação Pública)'''
        icms = 0.18 * base_tributavel
        pis_cofins = 0.095 * base_tributavel
        cosip = 20.0
        total = icms + pis_cofins + cosip
        return TarifasAdicionaisDTO(
            icms=icms,
            pis_cofins=pis_cofins, 
            cosip=cosip, 
            total=total
        )

    def calcular_tarifa(self, potencia: float, consumo_rede: float, geracao_kit: float) -> ContaNovaDTO:
        '''Função que calcula o valor líquido (compensação/injeção + taxas adicionais) sobre a energia de um kit de paineis solares.'''
        ano = int(date.today().strftime('%Y'))
        tusd = self.simulacao.concessionaria.tusd
        te = self.simulacao.concessionaria.te

        percentual_tusd = self.obter_percentual_tusd(ano)
        fio_b = 0.28
    
        # 1. Custo de Disponibilidade
        custo_disponibilidade = self.calcular_tarifa_disponibilidade(potencia=potencia, te=te, tusd=tusd)

        # 2. Cálculo do Consumo Bruto
        saldo_energia = geracao_kit - consumo_rede
        if (saldo_energia <= 0):
            energia_consumida = abs(saldo_energia)
            valor_energia = energia_consumida * (tusd + te)
            valor_bruto = valor_energia
        else:
            energia_injetada= saldo_energia
            valor_tusd_fio_b = energia_injetada * tusd * fio_b * percentual_tusd
            valor_bruto = max(custo_disponibilidade, valor_tusd_fio_b)
        
        # 3. Adição de Tarifas
        taxas = self.calcular_tarifas_adicionais(base_tributavel=valor_bruto)
        valor_liquido = valor_bruto + taxas.total

        return ContaNovaDTO(
            saldo_energia=saldo_energia,
            percentual_tusd=percentual_tusd,
            custo_disponibilidade=custo_disponibilidade,
            fio_b=fio_b,
            valor_bruto=valor_bruto,
            valor_liquido=valor_liquido,
            tarifas=taxas
        )

    def calcular_economia(self, economia_mensal: float) -> dict[str, float]:
        return EconomiaTotalDTO(
            mes_1=economia_mensal,
            mes_5=economia_mensal * 5,
            ano_1=economia_mensal * 12,
            ano_3=economia_mensal * 36,
            ano_5=economia_mensal * 60,
            ano_10=economia_mensal * 120 
        )
    
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

        return UsoPraticoDTO(
            num_lampadas=int(num_lampadas),
            num_geladeiras=int(num_geladeiras),
            num_lavagens=int(num_lavagens),
            autonomia_carro=int(autonomia_carro)
        )

    def calcular_viabilidade(self, perdas: float) -> SimulacaoDTO:
        '''Função que calcula a viabilidade da implementação de um determinado painel solar com base nos dados fornecidos pelo usuário (Simulacao). '''
        eficiencia_painel = self.simulacao.painel_solar.eficiencia / 100
        conta_luz_atual = self.simulacao.conta_luz      
        tarifa = self.simulacao.concessionaria.te + self.simulacao.concessionaria.tusd
        potencia_painel = self.simulacao.painel_solar.potencia
        area_disponivel = self.simulacao.area_disponivel
        valor_painel = self.simulacao.painel_solar.valor

        # Obter HSP
        hsp_mensal = self.simulacao.endereco.hsp

        # Consumo Atual
        consumo_usuario = conta_luz_atual / tarifa

        # Energia Gerada por Painel (kWh)
        energia_por_painel = (potencia_painel * hsp_mensal) / 1000 * (1 - perdas)

        # Área do Painel
        area_painel = potencia_painel / (1000 * eficiencia_painel)

        # Quantidade de Painéis 
        energia_total = 0
        min_paineis = 0
        area_total = 0
        max_paineis = int(area_disponivel // area_painel) # Obter Máximo com base na Área
        min_paineis = math.ceil(consumo_usuario / energia_por_painel) # Obter o número mínimo para suprir o consumo (ceil)
        qtd_paineis = min(max_paineis, min_paineis)

        # Energia Total Gerada
        energia_total = qtd_paineis * energia_por_painel
        
        # Área Ocupada  
        area_total = area_painel * qtd_paineis
        porcentagem_area = area_total * 100 / area_disponivel
        
        # Potência Total
        potencia_total = qtd_paineis * potencia_painel / 1000

        # Cálulo Financeiro
        percentual_acrescimos = 0.65
        investimento_paineis = valor_painel * qtd_paineis
        acrescimos = investimento_paineis / percentual_acrescimos
        total_investimento = investimento_paineis + acrescimos

        # Economia e Payback
        conta_final = self.calcular_tarifa(
            potencia=potencia_total,
            consumo_rede=consumo_usuario,
            geracao_kit=energia_total
        )
        economia_mensal = conta_luz_atual - conta_final.valor_liquido
        payback = total_investimento / economia_mensal
        economia_total = self.calcular_economia(economia_mensal)

        porcentagem_economia: float
        if (economia_mensal < conta_luz_atual):
            porcentagem_economia = (conta_luz_atual - conta_final.valor_liquido) * 100 / conta_luz_atual
        else:
            porcentagem_economia = (conta_final.valor_liquido - conta_luz_atual) * 100 / conta_final.valor_liquido

        # 6. Descobrir informações ecológicas
        uso_pratico = self.calcular_uso_pratico(energia_total)
        
        return SimulacaoDTO(
            conta_nova=conta_final,
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