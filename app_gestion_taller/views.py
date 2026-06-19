import json

from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt

from .forms import ContactoForm, ClienteForm, CocheForm, ServicioForm, CocheServicioForm
from .models import Cliente, Coche, Servicio, CocheServicio


def contacto(request):
    if request.method == 'POST':
        formulario = ContactoForm(request.POST)
        if formulario.is_valid():
            nombre = formulario.cleaned_data['nombre']
            return render(
                request,
                'app_gestion_taller/gracias.html',
                {'nombre': nombre},
            )
    else:
        formulario = ContactoForm()

    return render(
        request,
        'app_gestion_taller/contacto.html',
        {'formulario': formulario},
    )


def nuevo_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')
    else:
        form = ClienteForm()

    return render(
        request,
        'app_gestion_taller/formulario.html',
        {'form': form, 'titulo': 'Nuevo cliente'},
    )


def nuevo_coche(request):
    if request.method == 'POST':
        form = CocheForm(request.POST)
        if form.is_valid():
            coche = form.save()
            return redirect('detalle_cliente', cliente_id=coche.cliente.id)
    else:
        form = CocheForm()

    return render(
        request,
        'app_gestion_taller/formulario.html',
        {'form': form, 'titulo': 'Nuevo coche'},
    )


def nuevo_servicio(request):
    if request.method == 'POST':
        form = ServicioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')
    else:
        form = ServicioForm()

    return render(
        request,
        'app_gestion_taller/formulario.html',
        {'form': form, 'titulo': 'Nuevo servicio'},
    )


def nuevo_coche_servicio(request):
    if request.method == 'POST':
        form = CocheServicioForm(request.POST)
        if form.is_valid():
            coche_servicio = form.save()
            return redirect('buscar_servicios_de_coche', coche_id=coche_servicio.coche.id)
    else:
        form = CocheServicioForm()

    return render(
        request,
        'app_gestion_taller/formulario.html',
        {'form': form, 'titulo': 'Registrar servicio a un coche'},
    )


def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(
        request,
        'app_gestion_taller/lista_clientes.html',
        {'clientes': clientes},
    )


def detalle_cliente(request, cliente_id):
    try:
        cliente = Cliente.objects.get(id=cliente_id)
        coches = Coche.objects.filter(cliente=cliente)
        contexto = {
            'cliente': cliente,
            'coches': coches,
        }
        return render(request, 'app_gestion_taller/detalle_cliente.html', contexto)
    except Cliente.DoesNotExist:
        return JsonResponse({'error': 'Cliente no encontrado'}, status=404)


# Mantengo este nombre para conservar compatibilidad con la práctica anterior.
def buscar_cliente(request, cliente_id):
    return detalle_cliente(request, cliente_id)


@csrf_exempt
def registrar_cliente(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            cliente = Cliente.objects.create(
                nombre=data['nombre'],
                telefono=data['telefono'],
                email=data['email'],
            )
            return JsonResponse({
                'mensaje': 'Cliente registrado con éxito',
                'cliente_id': cliente.id,
            })
        except KeyError:
            return JsonResponse({'error': 'Datos incompletos'}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'JSON no válido'}, status=400)

    return JsonResponse({'error': 'Método no permitido'}, status=405)


@csrf_exempt
def registrar_coche(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            cliente = Cliente.objects.get(id=data['cliente_id'])
            coche = Coche.objects.create(
                cliente=cliente,
                marca=data['marca'],
                modelo=data['modelo'],
                matricula=data['matricula'],
            )
            return JsonResponse({
                'mensaje': 'Coche registrado con éxito',
                'coche_id': coche.id,
            })
        except Cliente.DoesNotExist:
            return JsonResponse({'error': 'Cliente no encontrado'}, status=404)
        except KeyError:
            return JsonResponse({'error': 'Datos incompletos'}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'JSON no válido'}, status=400)

    return JsonResponse({'error': 'Método no permitido'}, status=405)


@csrf_exempt
def registrar_servicio(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            coche = Coche.objects.get(id=data['coche_id'])
            servicio = Servicio.objects.create(
                nombre=data['nombre'],
                descripcion=data['descripcion'],
            )
            CocheServicio.objects.create(coche=coche, servicio=servicio)
            return JsonResponse({
                'mensaje': 'Servicio registrado con éxito',
                'servicio_id': servicio.id,
            })
        except Coche.DoesNotExist:
            return JsonResponse({'error': 'Coche no encontrado'}, status=404)
        except KeyError:
            return JsonResponse({'error': 'Datos incompletos'}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'JSON no válido'}, status=400)

    return JsonResponse({'error': 'Método no permitido'}, status=405)


@csrf_exempt
def buscar_coche_por_matricula(request, matricula):
    try:
        coche = Coche.objects.select_related('cliente').get(matricula=matricula)
        respuesta = {
            'coche': {
                'id': coche.id,
                'marca': coche.marca,
                'modelo': coche.modelo,
                'matricula': coche.matricula,
            },
            'cliente': {
                'id': coche.cliente.id,
                'nombre': coche.cliente.nombre,
                'telefono': coche.cliente.telefono,
                'email': coche.cliente.email,
            },
        }
        return JsonResponse(respuesta)
    except Coche.DoesNotExist:
        return JsonResponse({'error': 'Coche no encontrado'}, status=404)


@csrf_exempt
def buscar_coches_de_cliente(request, cliente_id):
    if not Cliente.objects.filter(id=cliente_id).exists():
        return JsonResponse({'error': 'Cliente no encontrado'}, status=404)

    coches = list(
        Coche.objects.filter(cliente_id=cliente_id).values(
            'id', 'marca', 'modelo', 'matricula'
        )
    )
    return JsonResponse(coches, safe=False)


@csrf_exempt
def buscar_servicios_de_coche(request, coche_id):
    try:
        coche = Coche.objects.get(id=coche_id)
        coche_servicios = (
            CocheServicio.objects.filter(coche=coche)
            .select_related('servicio')
        )
        contexto = {
            'coche': coche,
            'coche_servicios': coche_servicios,
        }
        return render(request, 'app_gestion_taller/servicios_coche.html', contexto)
    except Coche.DoesNotExist:
        return JsonResponse({'error': 'Coche no encontrado'}, status=404)
