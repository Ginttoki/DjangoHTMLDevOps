from django.urls import path
from . import views
from core.views import *

urlpatterns = [
    path('', index),
    path('listacursos/', listacursos),
    path('home/', home),
    path('detalhescurso/', detalhescurso),
    path('disciplinas/', disciplinas),
    path('noticias/', noticias),
]