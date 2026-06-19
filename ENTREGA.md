# Documento de entrega

**Alumno:** Javier Blanco Vila  
**Asignatura:** Arquitectura del Software  
**Repositorio:** `arquitectura_del_software`

## Enlace al repositorio

Pegar aquí el enlace al repositorio de GitHub:

```text
https://github.com/Javi54543/arquitectura_del_software
```

## Práctica inicial

La primera parte incluye:

- Proyecto Django llamado `mi_proyecto`.
- Aplicación Django llamada `primera_app`.
- Vista básica de bienvenida.
- Archivo `urls.py` dentro de la aplicación.
- Inclusión de las rutas de la aplicación en `mi_proyecto/urls.py`.
- Organización mediante ramas `main`, `develop` y `feature/primeraApp`.

## Práctica 3 - Base de datos

Al tratarse de una entrega incremental, se mantiene el proyecto anterior y se añade una nueva aplicación llamada `app_gestion_taller`.

La práctica 3 incluye:

- Alta de `app_gestion_taller` en `INSTALLED_APPS`.
- Inclusión de las rutas de la aplicación en `mi_proyecto/urls.py` bajo el prefijo `/gestion/`.
- Modelo `Cliente`, con nombre, teléfono y email.
- Modelo `Coche`, relacionado con `Cliente` mediante una relación 1-N.
- Modelo `Servicio`, relacionado con `Coche` mediante una relación N-N.
- Modelo intermedio `CocheServicio`, con coche, servicio y fecha.
- Migración inicial de base de datos para los modelos anteriores.
- Registro de los modelos en `admin.py`.
- Vista JSON para listar clientes.
- Vista JSON para consultar el detalle de un cliente por su identificador.

## Rutas principales

```text
http://127.0.0.1:8000/
http://127.0.0.1:8000/admin/
http://127.0.0.1:8000/gestion/clientes/
http://127.0.0.1:8000/gestion/clientes/1/
```

## Comandos de comprobación

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Para crear un administrador:

```bash
python manage.py createsuperuser
```
