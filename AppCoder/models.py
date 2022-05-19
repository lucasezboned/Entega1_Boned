from django.db import models

# Create your models here.

class Curso(models.Model):
    nombre= models.CharField(max_length=50)
    comision= models.IntegerField()

    def __str__(self):
        return self.nombre+" "+str(self.comision)

class Estudiante(models.Model):
    nombre= models.CharField(max_length=50)
    comision= models.IntegerField()
    email= models.EmailField()

class Profesor(models.Model):
    nombre= models.CharField(max_length=50)
    comision= models.CharField(max_length=50)


class EspacioEnAula(models.Model):
    institucion= models.CharField(max_length=50)
    espacio= models.IntegerField()
     
