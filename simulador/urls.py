from django.urls import path
from simulador.views import index

urlpatterns = [
    path('', index, name='iniciar_calculo')
]