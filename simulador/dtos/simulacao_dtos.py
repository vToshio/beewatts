from dataclasses import dataclass

@dataclass
class TarifasAdicionaisDTO:
    icms: float
    pis_cofins: float
    cosip: float
    total: float

@dataclass
class ContaNovaDTO:
    saldo_energia: float
    percentual_tusd: float
    fio_b: float
    custo_disponibilidade: float
    valor_liquido: float
    valor_bruto: float
    tarifas: TarifasAdicionaisDTO

@dataclass
class EconomiaTotalDTO:
    mes_1: float
    mes_5: float
    ano_1: float
    ano_3: float
    ano_5: float
    ano_10: float

@dataclass
class UsoPraticoDTO:
    num_lampadas: int
    num_geladeiras: int
    num_lavagens: int
    autonomia_carro: int


@dataclass
class SimulacaoDTO:
    conta_nova: ContaNovaDTO
    economia_total: EconomiaTotalDTO
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
    uso_pratico: UsoPraticoDTO