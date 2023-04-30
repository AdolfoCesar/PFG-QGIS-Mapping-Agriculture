from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

# Create your views here.
def registro(request):
    return render(request, 'registro.html')

def login(request):
    return render(request, 'login.html')