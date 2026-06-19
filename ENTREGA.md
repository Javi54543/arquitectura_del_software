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
