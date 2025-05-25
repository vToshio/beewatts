from django.contrib import admin
from simulador.models.concessionaria import Concessionaria

@admin.register(Concessionaria)
class ConcessionariaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'te', 'tusd', 'atualizada_em')
    list_display_links = ('id', 'nome', 'te', 'tusd', 'atualizada_em')
    search_fields = ('id', 'nome')
    fields = ('nome', 'te', 'tusd')
    