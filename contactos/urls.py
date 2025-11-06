from django.urls import path 
from . import views 

#Configurar URLs
urlpatterns = [
    path('', views.lista_contactos, name='lista_contactos'),
    path('nuevo/', views.nuevo_contacto, name='nuevo_contacto'),
    path('<int:contacto_id>/', views.detalle_contacto, name='detalle_contacto'),
    path('<int:contacto_id>/editar/', views.editar_contacto, name='editar_contacto'),
    path('<int:contacto_id>/eliminar/', views.eliminar_contacto, name='eliminar_contacto'),
    path('test/', views.test_view, name='test_view') 
]