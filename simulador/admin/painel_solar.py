from django.contrib import admin
from simulador.models.painel_solar import PainelSolar

@admin.register(PainelSolar)
class PainelSolarAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'potencia', 'eficiencia', 'data_consulta', 'link')
    list_display_links = ('id', 'nome', 'potencia', 'eficiencia', 'data_consulta', 'link')
    search_fields = ('id', 'nome', 'marca', 'potencia', 'data_consulta')
    fields = ('marca', 'valor', 'potencia', 'eficiencia', 'link')