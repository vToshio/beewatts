from django.urls import path
from simulador.views import index, endereco

urlpatterns = [
    path('', index, name='iniciar_calculo'),
    path('endereco/', endereco, name='cadastrar_endereco')
]