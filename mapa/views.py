from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
import os

# Create your views here.
def home(request):
    return render(request, 'home.html')

def mapaQGIS(request):
    ruta_archivo = os.path.join(settings.MEDIA_ROOT, 'service/datos.geojson')

    with open(ruta_archivo, 'r') as f:
        datos = f.read()
    return JsonResponse(datos, safe=False)

def informacionFormulario(request):
    return render(request, 'informacionFormulario.html')

def registro(request):
    return render(request, 'registro.html')

def login(request):
    return render(request, 'login.html')

def mapaGoogle(request):
    return render(request, 'mapaGoogle.html')

def about1(request):
    return render(request, 'about-1.html')

def mapDevol(request):
    return render(request, 'mapDevol.html')