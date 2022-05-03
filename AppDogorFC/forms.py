from django import forms

class JugadoresFormulario(forms.Form):

    nombreapellido = forms.CharField()
    posicion = forms.CharField()
    dorsalcamiseta = forms.IntegerField()

class CuerpoTecnicoFormulario(forms.Form):
    nombreapellido = forms.CharField()
    funcion = forms.CharField()

class JuntaFormulario(forms.Form):
    nombreapellido = forms.CharField()
    puesto = forms.CharField()
    email = forms.EmailField()
        