"""Rutas de la aplicación primera_app."""

from django.urls import path

from . import views

urlpatterns = [
    path('', views.bienvenida, name='bienvenida'),
    path('bienvenida/', views.bienvenida, name='bienvenida_detalle'),
]
