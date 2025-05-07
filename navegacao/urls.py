from django.urls import path
from navegacao.views import index

urlpatterns = [
    path('home/', index, name='home')    
]