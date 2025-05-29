from django.urls import path, include
from navegacao.views import index, sobre, teste, termo_privacidade
from simulador.urls import urlpatterns

urlpatterns = [
    path('', index, name='home'),
    path('sobre/', sobre, name='sobre'),
    path('teste/', teste, name='teste'),
    path('simulador/', include(urlpatterns)),
    path('uso-e-privacidade/', termo_privacidade, name='termos')
]