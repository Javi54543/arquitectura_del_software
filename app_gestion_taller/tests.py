from django.test import TestCase

from .models import Cliente


class ClienteViewsTest(TestCase):
    def test_lista_clientes_devuelve_json(self):
        Cliente.objects.create(
            nombre='Javier Blanco Vila',
            telefono='600000000',
            email='javier.blanco@example.com',
        )

        response = self.client.get('/gestion/clientes/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()[0]['nombre'], 'Javier Blanco Vila')

    def test_detalle_cliente_no_encontrado(self):
        response = self.client.get('/gestion/clientes/999/')

        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json(), {'error': 'Cliente no encontrado'})
