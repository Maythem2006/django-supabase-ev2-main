from django.contrib import admin
from .models import Contacto


@admin.register(Contacto)
class ContactoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'telefono', 'correo', 'direccion')
    search_fields = ('nombre', 'telefono', 'correo')
    list_filter = ('telefono',)
    ordering = ('nombre',)
    list_per_page = 25
    actions = ['marcar_sin_direccion']

    @admin.action(description="Marcar contactos sin dirección como '(Sin dirección)'")
    def marcar_sin_direccion(self, request, queryset):
        faltantes = queryset.filter(direccion__exact='')
        updated = faltantes.update(direccion='(Sin dirección)')
        self.message_user(request, f"{updated} contacto(s) actualizados sin dirección.")

