from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render (request, "index.html")

def home(request):
    return render (request, "home.html")

def disciplinas(request):
    return render (request, "disciplinas.html")

def detalhescurso(request):
    return render (request, "detalhescurso.html") 

def noticias(request):
    return render (request, "noticias.html")

def listacursos(request):
    return render (request, "listacursos.html")
# Create your views here.
