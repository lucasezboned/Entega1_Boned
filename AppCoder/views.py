from django import http
from django.shortcuts import render
from .models import Curso
from django.http import HttpResponse 
from .forms import *

# Create your views here.

def curso(self):
    curso=Curso(nombre="Curso de Django", comision=12345)
    curso.save()
    texto= f"Curso: {curso.nombre} comision: {curso.comision}"
    return HttpResponse(texto)


#def inicio(request):
 #   return render(request, 'AppCoder/inicio.html')

def profesores(request):
    return HttpResponse("esta es la pagina de profesores")

def estudiantes(request):
    return HttpResponse("esta es la pagina de estudiantes")

def cursos(request):
    return HttpResponse("esta es la pagina de cursos")

def entregables(request):
    return HttpResponse("esta es la pagina de entregables")

def inicio(request):
    if request.method == 'POST':
        miFormulario = CursoFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            curso = Curso (nombre=informacion['nombre'], comision=informacion['comision'])
            curso.save()
            return render(request, 'AppCoder/inicio.html')
    else:
        miFormulario=CursoFormulario()
    return render(request, 'AppCoder/inicio.html', {'miFormulario':miFormulario})

def busquedaCamada(request):
    return render(request, 'AppCoder/busquedaCamada.html')

def buscar(request):
    if request.GET['comision']:
        comision = request.GET['comision']
        cursos = Curso.objects.filter(comision=comision)
        return render(request, 'AppCoder/resultadosBusqueda.html', {'cursos':cursos})
    else:
        respuesta = f"Estoy buscando la camada"
    return HttpResponse(respuesta)