from django.urls import path
from simulador.views import index, endereco, dados_iniciais, resultados

urlpatterns = [
    path('', index, name='iniciar_calculo'),
    path('endereco/', endereco, name='registrar_endereco'),
    path('dados-iniciais/', dados_iniciais, name='registrar_dados'),
    path('resultados/<uuid:id>', resultados, name='visualizar_resultados')
]