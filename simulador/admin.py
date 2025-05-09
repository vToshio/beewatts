from django.contrib import admin
from simulador.models.endereco import Endereco

# Register your models here.
@admin.register(Endereco)
class EnderecoAdmin(admin.ModelAdmin):
    list_display = ('id', 'cep', 'uf', 'cidade', 'bairro')
    list_display_links = ('id', 'cep', 'uf', 'cidade', 'bairro')
    search_fields = ('cep', 'uf', 'cidade', 'bairro')
    fields = ('cep', 'uf', 'cidade', 'bairro')