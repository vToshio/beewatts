from django.urls import path, include
from navegacao.views import index, sobre
from simulador.urls import urlpatterns

urlpatterns = [
    path('home/', index, name='home'),
    path('sobre/', sobre, name='sobre'),
    path('simulador/', include(urlpatterns))
]