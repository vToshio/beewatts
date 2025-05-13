from django.contrib import admin
from .models.endereco import Endereco
from .models.cidade import Cidade
from .models.estado import Estado

# Register your models here.
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

    
@admin.register(Cidade)
class CidadeAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'get_sigla')
    list_display_links = ('id', 'nome', 'get_sigla')
    search_fields = ('id', 'nome', 'get_sigla')

    def get_sigla(self, obj: Cidade):
        return obj.estado.sigla
    get_sigla.short_description = 'UF'

    def has_add_permission(self, request):
        return False
    
    def has_change_permission(self, request, obj = ...):
        return False