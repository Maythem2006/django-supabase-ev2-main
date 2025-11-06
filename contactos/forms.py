from django import forms
from .models import Contacto

#Definir un formulario para el modelo contactos, para crear y editar los contactos
class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ['nombre', 'telefono', 'correo', 'direccion']
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Nombre completo'}),
            'telefono': forms.TextInput(attrs={'placeholder': '9 o 2 1234 5678'}),
            'correo': forms.EmailInput(attrs={'placeholder': 'ejemplo@correo.com'}),
            'direccion': forms.TextInput(attrs={'placeholder': 'Dirección'}),
        }