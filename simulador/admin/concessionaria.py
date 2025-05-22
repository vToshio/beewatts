from django.contrib import admin
from simulador.models.concessionaria import Concessionaria

@admin.register(Concessionaria)
class ConcessionariaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'tarifa')
    list_display_links = ('id', 'nome', 'tarifa')
    search_fields = ('id', 'nome')

    