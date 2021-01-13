from django import forms

class FormularioContacto(forms.Form):
    nombre=forms.CharField(label='Nombre', required=True, max_length=20)
    email=forms.EmailField(label='Email', required=True)
    contenido=forms.CharField(label='Contenido', required=True, max_length=100, widget=forms.Textarea)
