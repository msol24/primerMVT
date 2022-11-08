
from django.shortcuts import render
from .models import Pariente
# Create your views here.

def show_index(request):
    Papa= Pariente(nombre='Jose Luis', apellido='Pucciarelli', parentesco='Papa', edad=75)
    Mama = Pariente(nombre='Graciela', apellido='Zani', parentesco='Mama', edad=70)
    Hermano= Pariente(nombre='Agustin', apellido='Pucciarelli', parentesco='Hermano', edad=40)

    return render(request, 'index.html', {'objetos': [Papa, Mama, Hermano]})