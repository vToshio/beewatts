from django.contrib import admin
from simulador.models.painel_solar import PainelSolar

@admin.register(PainelSolar)
class PainelSolarAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'potencia', 'altura', 'largura', 'data_consulta', 'link')
    list_display_links = ('id', 'nome', 'potencia', 'altura', 'largura', 'data_consulta', 'link')
    search_fields = ('id', 'nome', 'potencia', 'data_consulta')
    fields = ('valor', 'potencia', 'altura', 'largura', 'link')