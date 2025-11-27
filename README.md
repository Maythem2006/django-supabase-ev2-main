# Agenda de Contactos - Django REST API

Un proyecto Django que implementa una aplicación de gestión de contactos con operaciones CRUD completas, autenticación JWT y API REST.

## 📋 Características

- **Gestión de Contactos**: Crear, leer, actualizar y eliminar contactos
- **Búsqueda Avanzada**: Búsqueda de contactos por nombre, teléfono o correo
- **Validaciones**: 
  - Validación de números de teléfono chilenos (9 dígitos, comienzan con 2 o 9)
  - Validación de correos electrónicos
- **API REST**: Endpoints RESTful con Django REST Framework
- **Autenticación**: Autenticación JWT (Simple JWT)
- **Admin Panel**: Panel administrativo de Django integrado

## 🛠️ Tecnologías

- **Django 5.2.7**: Framework web principal
- **Django REST Framework**: API REST
- **djangorestframework-simplejwt**: Autenticación JWT
- **PostgreSQL** (psycopg2): Base de datos
- **WhiteNoise**: Servicio de archivos estáticos
- **Gunicorn**: Servidor WSGI
- **Python Dotenv**: Gestión de variables de entorno

## 📁 Estructura del Proyecto

```
django-supabase-ev2/
├── agenda/                 # Configuración del proyecto
│   ├── settings.py        # Configuración de Django
│   ├── urls.py            # URLs principales
│   ├── asgi.py            # Configuración ASGI
│   ├── wsgi.py            # Configuración WSGI
│
├── contactos/             # Aplicación principal de contactos
│   ├── models.py          # Modelos de datos
│   ├── views.py           # Vistas y ViewSets
│   ├── serializers.py     # Serializadores REST
│   ├── forms.py           # Formularios Django
│   ├── urls.py            # URLs de la aplicación
│   ├── admin.py           # Configuración del admin
│   ├── apps.py            # Configuración de la app
│   ├── migrations/        # Migraciones de base de datos
│   └── templates/         # Plantillas HTML
│       └── contactos/
│           ├── base.html
│           ├── lista_contactos.html
│           ├── nuevo_contacto.html
│           ├── editar_contactos.html
│           ├── detalle_contactos.html
│           └── eliminar_contactos.html
│
├── staticfiles/           # Archivos estáticos (admin, REST framework)
├── manage.py             # Script de gestión de Django
├── requirements.txt      # Dependencias del proyecto
└── README.md            # Este archivo
```

## 📊 Modelo de Datos

### Contacto
```python
- nombre (CharField, max_length=100)
- telefono (CharField, max_length=9)
  - Validación: Debe ser formato chileno (ej: 912345678)
- correo (CharField, max_length=100)
  - Validación: Formato de email válido
- direccion (TextField, optional)
```

## 🚀 Instalación y Configuración

### Requisitos Previos
- Python 3.8+
- pip
- PostgreSQL (opcional, SQLite en desarrollo)

### Pasos de Instalación

1. **Clonar el repositorio**
```bash
git clone <repositorio>
cd django-supabase-ev2
```

2. **Crear entorno virtual**
```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac
```

3. **Instalar dependencias**
```bash
pip install -r requirements.txt
```

4. **Configurar variables de entorno**
```bash
# Crear archivo .env
copy .env.example .env
```

5. **Aplicar migraciones**
```bash
python manage.py migrate
```

6. **Crear superusuario**
```bash
python manage.py createsuperuser
```

7. **Ejecutar servidor de desarrollo**
```bash
python manage.py runserver
```

## 📡 API Endpoints

### Endpoints REST
- `GET/POST /api/contactos/` - Listar/crear contactos
- `GET/PUT/DELETE /api/contactos/{id}/` - Detalle/actualizar/eliminar contacto
- `GET/POST /api/users/` - Gestión de usuarios
- `GET/POST /api/groups/` - Gestión de grupos

### Vistas Tradicionales
- `GET /contactos/` - Listar contactos con buscador
- `GET /contactos/nuevo/` - Formulario para nuevo contacto
- `POST /contactos/nuevo/` - Guardar nuevo contacto
- `GET /contactos/<id>/` - Detalle del contacto
- `GET /contactos/<id>/editar/` - Formulario de edición
- `POST /contactos/<id>/editar/` - Guardar cambios
- `GET /contactos/<id>/eliminar/` - Confirmar eliminación
- `POST /contactos/<id>/eliminar/` - Eliminar contacto

## 🔐 Autenticación

La API utiliza **JWT (JSON Web Tokens)** para autenticación:

```bash
# Obtener token
POST /api/token/
{
  "username": "usuario",
  "password": "contraseña"
}

# Usar token en headers
Authorization: Bearer <token>
```

## 📝 Formularios

### ContactoForm
Formulario para crear y editar contactos con validaciones automáticas:
- Validación de campos requeridos
- Validación de formato de teléfono
- Validación de formato de email

## 🎨 Plantillas

Las plantillas están ubicadas en `contactos/templates/contactos/`:
- **base.html**: Plantilla base con navegación
- **lista_contactos.html**: Listado de contactos con buscador
- **nuevo_contacto.html**: Formulario para crear contacto
- **editar_contactos.html**: Formulario para editar contacto
- **detalle_contactos.html**: Vista detallada de un contacto
- **eliminar_contactos.html**: Confirmación de eliminación

## ⚙️ Configuración Importante

### Settings Principales (agenda/settings.py)
- **DEBUG**: False (producción)
- **ALLOWED_HOSTS**: onrender.com, 127.0.0.1
- **INSTALLED_APPS**: Incluye contactos y REST Framework
- **DATABASES**: Configurada para PostgreSQL en producción
- **STATIC_FILES**: Servidos por WhiteNoise

## 📦 Despliegue

El proyecto está configurado para desplegarse en **Render.com**:
- Utiliza Gunicorn como servidor WSGI
- WhiteNoise para servir archivos estáticos
- Variables de entorno para configuración sensible

## 🔍 Búsqueda y Filtros

La aplicación incluye búsqueda avanzada que filtra contactos por:
- Nombre (búsqueda insensible a mayúsculas)
- Teléfono
- Correo electrónico

Utiliza `django.db.models.Q` para consultas OR complejas.

## 📚 Dependencias

Ver `requirements.txt` para la lista completa de dependencias:
- django
- djangorestframework
- djangorestframework-simplejwt
- psycopg2
- gunicorn
- whitenoise
- python-dotenv
- openpyxl

## 🤝 Contribuir

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo licencia MIT.

## ✉️ Contacto

Para preguntas o sugerencias, contacta al equipo de desarrollo.

---

**Última actualización**: Noviembre 2025
