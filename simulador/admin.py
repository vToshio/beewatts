from django.contrib import admin
from .models.endereco import Endereco

# Register your models here.
@admin.register(Endereco)
class EnderecoAdmin(admin.ModelAdmin):
    list_display = ('id', 'cep', 'uf', 'cidade', 'logradouro')
    list_display_links = ('id', 'cep', 'uf', 'cidade', 'logradouro')
    search_fields = ('cep', 'uf', 'cidade', 'logradouro')
    fields = ('cep', 'uf', 'cidade', 'logradouro')

    def has_add_permission(self, request):
        return False