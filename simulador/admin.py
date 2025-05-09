from django.contrib import admin
from .models.endereco import Endereco
from .models.cidade import Cidade

# Register your models here.
@admin.register(Endereco)
class EnderecoAdmin(admin.ModelAdmin):
    list_display = ('id', 'cep', 'uf', 'cidade__nome', 'logradouro')
    list_display_links = ('id', 'cep', 'uf', 'cidade__nome', 'logradouro')
    search_fields = ('cep', 'uf', 'cidade__nome', 'logradouro')
    fields = ('cep', 'uf', 'cidade__nome', 'logradouro')

    def has_add_permission(self, request):
        return False

@admin.register(Cidade)
class CidadeAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    fields = ('nome',)

    def has_add_permission(self, request):
        return False