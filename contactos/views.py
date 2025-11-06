#Crear las vistas funcionales para manjear las operaciones CRUD
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .models import Contacto
from .forms import ContactoForm

# LISTAR + BUSCADOR VIA Import Q = query
def lista_contactos(request):
    query = request.GET.get('q')  
    if query:
        contactos = Contacto.objects.filter(
            Q(nombre__icontains=query) |
            Q(telefono__icontains=query) |
            Q(correo__icontains=query)  
        )
    else:
        contactos = Contacto.objects.all()
    
    return render(request, 'contactos/lista_contactos.html', {'contactos': contactos, 'query': query})

# CREAR CONTACTO
def nuevo_contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_contactos')
    else:
        form = ContactoForm()
    return render(request, 'contactos/nuevo_contacto.html', {'form': form})

# DETALLE CONTACTO
def detalle_contacto(request, contacto_id):
    contacto = get_object_or_404(Contacto, id=contacto_id)
    return render(request, 'contactos/detalle_contactos.html', {'contacto': contacto})

# EDITAR CONTACTO
def editar_contacto(request, contacto_id):
    contacto = get_object_or_404(Contacto, id=contacto_id)
    if request.method == 'POST':
        form = ContactoForm(request.POST, instance=contacto)
        if form.is_valid():
            form.save()
            return redirect('lista_contactos')
    else:
        form = ContactoForm(instance=contacto)
    return render(request, 'contactos/editar_contactos.html', {'form': form})

# ELIMINAR CONTACTO
def eliminar_contacto(request, contacto_id):
    contacto = get_object_or_404(Contacto, id=contacto_id)
    if request.method == 'POST':
        contacto.delete()
        return redirect('lista_contactos')
    return render(request, 'contactos/eliminar_contactos.html', {'contacto': contacto})


from django.shortcuts import render

def test_view(request):
    return render(request, 'contactos/test.html')

