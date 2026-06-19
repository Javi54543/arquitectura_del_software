# Documento de entrega

**Alumno:** Javier Blanco Vila  
**Asignatura:** Arquitectura del Software  
**Práctica:** Desarrollo de una Aplicación Django con Control de Versiones en GitHub

## Enlace al repositorio

Pegar aquí el enlace al repositorio de GitHub:

```text
https://github.com/usuario/arquitectura_del_software
```

## Contenido entregado

La práctica incluye:

- Proyecto Django llamado `mi_proyecto`.
- Aplicación Django llamada `primera_app`.
- Vista básica de bienvenida en `primera_app/views.py`.
- Archivo `urls.py` dentro de la aplicación.
- Inclusión de las rutas de la aplicación en `mi_proyecto/urls.py`.
- Archivo `requirements.txt` con Django.
- Archivo `.gitignore` para evitar subir entorno virtual, cachés y base de datos local.
- Organización mediante ramas `main`, `develop` y `feature/primeraApp`.

## Comprobación

Para comprobar que funciona:

```bash
pip install -r requirements.txt
python manage.py runserver
```

Después entrar en:

```text
http://127.0.0.1:8000/
```

Debe aparecer el mensaje de bienvenida de la aplicación.
