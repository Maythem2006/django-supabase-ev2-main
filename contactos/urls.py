from django.urls import path, include
from . import views 
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r"users", views.UserViewSet)
router.register(r"groups", views.GroupViewSet)
#Configurar URLs
urlpatterns = [
    path("api/", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path('', views.lista_contactos, name='lista_contactos'),
    path('nuevo/', views.nuevo_contacto, name='nuevo_contacto'),
    path('<int:contacto_id>/', views.detalle_contacto, name='detalle_contacto'),
    path('<int:contacto_id>/editar/', views.editar_contacto, name='editar_contacto'),
    path('<int:contacto_id>/eliminar/', views.eliminar_contacto, name='eliminar_contacto'),
    path('test/', views.test_view, name='test_view') 
]