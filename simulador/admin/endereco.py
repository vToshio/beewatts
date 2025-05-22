from django.contrib import admin
from simulador.models.endereco import Endereco

@admin.register(Endereco)
class EnderecoAdmin(admin.ModelAdmin):
    list_display = ('id', 'cep', 'get_sigla', 'get_cidade', 'logradouro')
    list_display_links = ('id', 'cep', 'get_sigla', 'get_cidade', 'logradouro')
    search_fields = ('cep', 'get_sigla', 'get_cidade', 'logradouro')

    def get_sigla(self, obj: Endereco):
        return obj.cidade.estado.sigla
    get_sigla.short_description = 'UF'
    
    def get_cidade(self, obj: Endereco):
        return obj.cidade.nome
    get_cidade.short_description = 'Cidade'

    def has_add_permission(self, request):
        return False
    
    def has_change_permission(self, request, obj = ...):
        return False