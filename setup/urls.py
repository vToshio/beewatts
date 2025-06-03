"""
URL configuration for setup project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from navegacao.urls import urlpatterns

urlpatterns = [
    path('pagina-secreta/', admin.site.urls, name='admin'),
    path('', include(urlpatterns))  
]

handler400 = 'navegacao.views.requisicao_invalida'
handler403 = 'navegacao.views.acesso_proibido'
handler404 = 'navegacao.views.pagina_nao_encontrada'
handler500 = 'navegacao.views.erro_interno'