from django.db import models
from django.core.validators import EmailValidator
from django.core.validators import RegexValidator

# Crear los modelos para la aplicacion contactos 

class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(
        max_length=9,
        validators=[    #validador de caracteres 
            RegexValidator( 
                regex=r'^[29]\d{8}$',
                message="El número debe comenzar con 2 (casa) o 9 (móvil) y tener 9 digitos."
            )
        ]
    )
    correo = models.CharField(
        max_length=100,
        validators=[EmailValidator(message="Correo inválido")] #validador e invalida el correo al equivocarse 
    )
    direccion = models.TextField(blank=True)

    def __str__(self):
        return f"{self.nombre} - {self.correo}"


