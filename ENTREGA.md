# Práctica 6 - Formularios en Django

Alumno: Javier Blanco Vila

Repositorio:
https://github.com/Javi54543/arquitectura_del_software

## Contenido añadido

En esta práctica se añaden formularios al proyecto incremental del taller de coches.

Se ha incorporado el archivo `forms.py` en la aplicación `app_gestion_taller` con:

- `ContactoForm`, formulario manual sin modelo.
- `ClienteForm`, basado en el modelo `Cliente`.
- `CocheForm`, basado en el modelo `Coche`.
- `ServicioForm`, basado en el modelo `Servicio`.
- `CocheServicioForm`, basado en el modelo `CocheServicio`.

También se han añadido vistas y plantillas para crear registros desde formularios HTML:

- `/gestion/contacto/`
- `/gestion/clientes/nuevo/`
- `/gestion/coches/nuevo/`
- `/gestion/servicios/nuevo/`
- `/gestion/coche-servicio/nuevo/`

Las vistas anteriores de listado, detalle y servicios se mantienen, junto con los endpoints JSON de prácticas anteriores.
