from django.contrib import admin
from simulador.models.cidade import Cidade

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