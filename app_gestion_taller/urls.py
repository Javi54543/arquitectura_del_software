from django.urls import path

from .views import (
    buscar_coche_por_matricula,
    buscar_coches_de_cliente,
    buscar_servicios_de_coche,
    contacto,
    detalle_cliente,
    lista_clientes,
    nuevo_cliente,
    nuevo_coche,
    nuevo_coche_servicio,
    nuevo_servicio,
    registrar_cliente,
    registrar_coche,
    registrar_servicio,
)

urlpatterns = [
    path('clientes/', lista_clientes, name='lista_clientes'),
    path('clientes/nuevo/', nuevo_cliente, name='nuevo_cliente'),
    path('coches/nuevo/', nuevo_coche, name='nuevo_coche'),
    path('servicios/nuevo/', nuevo_servicio, name='nuevo_servicio'),
    path('coche-servicio/nuevo/', nuevo_coche_servicio, name='nuevo_coche_servicio'),
    path('contacto/', contacto, name='contacto'),
    path('clientes/registrar/', registrar_cliente, name='registrar_cliente'),
    path('coches/registrar/', registrar_coche, name='registrar_coche'),
    path('servicios/registrar/', registrar_servicio, name='registrar_servicio'),
    path('clientes/<int:cliente_id>/', detalle_cliente, name='detalle_cliente'),
    path('coches/matricula/<str:matricula>/', buscar_coche_por_matricula, name='buscar_coche_por_matricula'),
    path('clientes/<int:cliente_id>/coches/', buscar_coches_de_cliente, name='buscar_coches_de_cliente'),
    path('coches/<int:coche_id>/servicios/', buscar_servicios_de_coche, name='buscar_servicios_de_coche'),
]
