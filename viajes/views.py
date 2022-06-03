from django.shortcuts import render
from viajes.models import Viaje
# Create your views here.

def listar_viaje(request):
    lista_viaje = Viaje.objects.all()
    context = {'lista_viaje' : lista_viaje}
    return render(request, 'listar_viajes.html', context=context)