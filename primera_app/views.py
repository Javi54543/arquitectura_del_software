"""Vistas de la aplicación primera_app."""

from django.http import HttpResponse


def bienvenida(request):
    """Devuelve un mensaje básico de bienvenida para comprobar la aplicación."""
    return HttpResponse(
        '<h1>Bienvenido a la primera aplicación Django</h1>'
        '<p>Práctica de Arquitectura del Software realizada con Django y GitHub.</p>'
    )
