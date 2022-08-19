from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def misionVision(request):
    return render(request, 'mision-vision.html')

def quienesSomos(request):
    return render(request, 'quines somos.html')

def recursos(request):
    return render(request, 'recursos.html')

def noticias(request):
    return render(request, 'noticias.html')

def eventos(request):
    return render(request, 'eventos.html')