from django.contrib import admin
from simulador.models.painel_solar import PainelSolar

@admin.register(PainelSolar)
class PainelSolarAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'potencia', 'altura', 'largura', 'area')
    list_display_links = ('id', 'nome', 'potencia', 'altura', 'largura', 'area')
    search_fields = ('id', 'nome', 'potencia', 'area')
    fields = ('valor', 'potencia', 'altura', 'largura')