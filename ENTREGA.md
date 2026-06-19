# Entrega incremental - Práctica Django

Alumno: Javier Blanco Vila

Repositorio:
https://github.com/Javi54543/arquitectura_del_software

## Práctica inicial

Se creó el proyecto Django base con una primera aplicación, rutas básicas y control de versiones con ramas `main`, `develop` y `feature/primeraApp`.

## Práctica 3 - Base de datos

Se añadió la aplicación `app_gestion_taller` para gestionar una base de datos de un taller de coches.

Elementos incluidos:

- Modelo `Cliente` con nombre, teléfono y email.
- Modelo `Coche` relacionado con `Cliente` mediante una relación 1-N.
- Modelo `Servicio` relacionado con `Coche` mediante una relación N-N.
- Modelo intermedio `CocheServicio` para registrar qué servicio recibe cada coche.
- Registro de los modelos en `admin.py`.
- Vistas JSON para listar clientes y consultar un cliente por ID.
- Rutas bajo `/gestion/`.

## Práctica 4 - Endpoints de registro y búsqueda

Se añadieron endpoints para registrar clientes, coches y servicios mediante peticiones POST, y endpoints de consulta mediante peticiones GET.

### Endpoints POST

- `POST /gestion/clientes/registrar/`
- `POST /gestion/coches/registrar/`
- `POST /gestion/servicios/registrar/`

### Endpoints GET

- `GET /gestion/clientes/`
- `GET /gestion/clientes/<id>/`
- `GET /gestion/coches/matricula/<matricula>/`
- `GET /gestion/clientes/<id>/coches/`
- `GET /gestion/coches/<id>/servicios/`

### Ejemplos de prueba con cURL

Registrar cliente:

```bash
curl -X POST http://127.0.0.1:8000/gestion/clientes/registrar/ \
-H "Content-Type: application/json" \
-d '{"nombre": "Juan Perez", "telefono": "123456789", "email": "juan@example.com"}'
```

Registrar coche:

```bash
curl -X POST http://127.0.0.1:8000/gestion/coches/registrar/ \
-H "Content-Type: application/json" \
-d '{"cliente_id": 1, "marca": "Toyota", "modelo": "Corolla", "matricula": "XYZ123"}'
```

Registrar servicio:

```bash
curl -X POST http://127.0.0.1:8000/gestion/servicios/registrar/ \
-H "Content-Type: application/json" \
-d '{"coche_id": 1, "nombre": "Cambio de aceite", "descripcion": "Cambio de aceite sintetico"}'
```

## Práctica 5 - Plantillas en Django

Se añadieron plantillas HTML para que varias vistas del taller de coches dejen de devolver únicamente JSON y pasen a mostrar páginas web renderizadas con Django.

Elementos incluidos:

- Configuración de `TEMPLATES['DIRS']` con `BASE_DIR / 'templates'`.
- Carpeta `templates/app_gestion_taller/`.
- Plantilla base `base.html` con herencia de plantillas.
- Plantilla `lista_clientes.html` para mostrar todos los clientes en una tabla.
- Enlace desde el nombre de cada cliente hacia su página de detalle.
- Plantilla `detalle_cliente.html` para mostrar los datos del cliente y sus coches registrados.
- Plantilla `servicios_coche.html` para mostrar los servicios realizados a un coche.
- Uso de etiquetas de plantilla `{{ variable }}`, `{% if %}`, `{% else %}`, `{% for %}` y `{% url %}`.

### Vistas HTML

- `GET /gestion/clientes/`
- `GET /gestion/clientes/<id>/`
- `GET /gestion/coches/<id>/servicios/`

Los endpoints POST de la práctica anterior se mantienen para registrar clientes, coches y servicios.
