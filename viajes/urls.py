from django.urls import path
from viajes.views import listar_viaje

urlpatterns = [
    path('', listar_viaje, name = 'listar_viaje')
]