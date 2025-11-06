#Incluir las vistas solicitadas por la app contactos
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('contactos.urls')),  
]

