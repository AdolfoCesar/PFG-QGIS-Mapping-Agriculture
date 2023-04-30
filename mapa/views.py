from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def mapaQGIS(request):
    return render(request, 'mapaQGIS.html')

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