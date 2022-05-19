from django import forms



class CursoyProfesFormulario(forms.Form):
    #especificamos los campos del formulario
    nombre= forms.CharField(max_length=50)
    comision= forms.IntegerField()
    


class EspacioEnAulaFormulario(forms.Form):
    #especificamos los campos del formulario
    institucion= forms.CharField(max_length=50)
    espacio= forms.IntegerField()
    