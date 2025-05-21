from django.contrib import admin
from simulador.models.simulacao import Simulacao

@admin.register(Simulacao)
class SimulacaoAdmin(admin.ModelAdmin):
    list_display = ('get_endereco', 'get_painel', 'get_concessionaria', 'total_investimento', 'tempo_payback', 'area_total', 'custo_beneficio')
    list_display_links = ('get_endereco', 'get_painel', 'get_concessionaria', 'total_investimento', 'tempo_payback', 'area_total', 'custo_beneficio')
    search_fields = ('endereco__cidade__nome', 'endereco__cidade__estado__sigla', 'concessionaria__nome')

    def get_painel(self, obj: Simulacao):
        return obj.painel_solar.nome
    get_painel.short_description = 'Painel Solar'
    
    def get_endereco(self, obj: Simulacao):
        return f'{obj.endereco.cidade.nome} ({obj.endereco.cidade.estado.sigla})'
    get_endereco.short_description = 'Endereço'

    def get_concessionaria(self, obj: Simulacao):
        return obj.concessionaria.nome
    get_concessionaria.short_description = 'Concessionária'

    def has_add_permission(self, request):
        return False
    
    def has_change_permission(self, request, obj = ...):
        return False