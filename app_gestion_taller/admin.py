from django.contrib import admin

from .models import Cliente, Coche, Servicio, CocheServicio


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'telefono', 'email')
    search_fields = ('nombre', 'telefono', 'email')


@admin.register(Coche)
class CocheAdmin(admin.ModelAdmin):
    list_display = ('id', 'marca', 'modelo', 'matricula', 'cliente')
    search_fields = ('marca', 'modelo', 'matricula', 'cliente__nombre')
    list_filter = ('marca',)


@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    search_fields = ('nombre', 'descripcion')


@admin.register(CocheServicio)
class CocheServicioAdmin(admin.ModelAdmin):
    list_display = ('id', 'coche', 'servicio', 'fecha')
    search_fields = ('coche__matricula', 'servicio__nombre')
    list_filter = ('fecha', 'servicio')
