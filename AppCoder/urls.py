from django.urls import path
from .views import *


urlpatterns = [
    path('', inicio),
    
    path('creaCurso', curso),
    
    path('cursos/', cursos),
    path('profesores/', profesores),
    path('estudiantes/', estudiantes),
    path('entregables/', entregables),
    path('busquedaCamada/', busquedaCamada, name='BusquedaCamada'),
    path('buscar/', buscar),
    path('resultadosBusqueda/', buscar)
     ]
    

