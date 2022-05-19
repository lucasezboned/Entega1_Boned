from django import http
from django.shortcuts import render
from .models import Curso, Profesor, EspacioEnAula
from django.http import HttpResponse
from AppCoder.forms import CursoyProfesFormulario, EspacioEnAulaFormulario

# Create your views here.

def curso(self):
    curso=Curso(nombre="Curso de Django", comision=12345)
    curso.save()
    texto= f"Curso: {curso.nombre} comision: {curso.comision}"
    return HttpResponse(texto)

    


def inicio(request):
    return render(request, 'AppCoder/inicio.html')

def profesores(request):
    return render(request, 'AppCoder/profesores.html')

def estudiantes(request):
    return render(request, 'AppCoder/estudiantes.html')




#-----------------------------------------------------------------------------
def cursos(request):

    if request.method == 'POST':

        miFormulario=CursoyProfesFormulario(request.POST)

        if miFormulario.is_valid():
            informacion=miFormulario.cleaned_data
            curso=Curso(nombre=informacion['nombre'], comision=informacion['comision'])
            curso.save()
            return render(request, 'AppCoder/inicio.html')

    else:
        miFormulario=CursoyProfesFormulario()
    return render(request, 'AppCoder/cursos.html', {'formulario':miFormulario})
#-------------------------------------------------------------------


def profesores(request):

    if request.method == 'POST':

        miFormulario=CursoyProfesFormulario(request.POST)

        if miFormulario.is_valid():
            informacion=miFormulario.cleaned_data
            profesor=Profesor(nombre=informacion['nombre'], comision=informacion['comision'])
            profesor.save()
            return render(request, 'AppCoder/inicio.html')

    else:
        miFormulario=CursoyProfesFormulario()
    return render(request, 'AppCoder/profesores.html', {'formulario':miFormulario})






def espacioenaulas(request):

    if request.method == 'POST':

        miFormulario=EspacioEnAulaFormulario(request.POST)

        if miFormulario.is_valid():
            informacion=miFormulario.cleaned_data
            espacioenaula=EspacioEnAula(espacio=informacion['espacio'], institucion=informacion['institucion'])
            espacioenaula.save()
            return render(request, 'AppCoder/inicio.html')

    else:
        miFormulario=EspacioEnAulaFormulario()
    return render(request, 'AppCoder/espacioenaulas.html', {'formulario':miFormulario})










def busquedaComision(request):
    return render(request, 'AppCoder/busquedaComision.html')


def buscar(request):
    if request.GET['comision']:
        comision=request.GET['comision']
        cursos=Curso.objects.filter(comision=comision)

        return render(request, 'AppCoder/resultadosBusqueda.html', {'cursos':cursos, 'comision':comision})
    else:
        respuesta="No se ingreso ninguna comision"
        return render(request, 'AppCoder/resultadosBusqueda.html', {'respuesta':respuesta})

        
    return render(request, 'AppCoder/cursosFormulario.html')