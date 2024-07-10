from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from electronic_network.models import SupplierNode, Contacts, Product
from users.models import User


class ElectronicNetworkTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(
            email='test@test.test',
            password='test',
            is_active=True,
        )

        self.client.force_authenticate(user=self.user)

        self.supplier = SupplierNode.objects.create(
            name='test-name',
            type='factory',
            supplier=None,
        )

        self.contacts = Contacts.objects.create(
            supplier=self.supplier,
            email='test-email',
            country='test-country',
            city='test-city',
            street='test-street',
            house='test-house'
        )

        self.product = Product.objects.create(
            name='product-name',
            model='product-model',

        )

        self.supplier.products.set([self.product])

    def test_create_supplier(self):
        data = {
            'name': 'test-name',
            'type': 'factory',
        }
        response = self.client.post('/create/', data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        supplier_id = response.json()['id']

        data = {
            'supplier': supplier_id,
            'email': 'test@email.com',
            'country': 'test-country',
            'city': 'test-city',
            'street': 'test-street',
            'house': 'test-house'
        }
        response = self.client.post('/contacts/create/', data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        data = {
            'supplier': supplier_id,
            'name': 'product-name',
            'model': 'product-model'
        }

        response = self.client.post('/products/create/', data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.get('/detail/1/', data=data)
        print(response.json())

    def test_update_supplier(self):
        data = {
            'name': 'test-name2',
            'type': 'factory',
        }

        response = self.client.patch(f'/update/{self.supplier.pk}/', data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = {
            'email': 'test@email.com',
            'country': 'test-country2',
            'city': 'test-city2',
            'street': 'test-street',
            'house': 'test-house'
        }
        response = self.client.patch(f'/contacts/update/{self.contacts.pk}/', data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = {
            'name': 'product-name2',
            'model': 'product-model2'
        }

        response = self.client.patch(f'/products/update/{self.product.pk}/', data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_supplier(self):
        response = self.client.delete(f'/delete/{self.supplier.pk}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        response = self.client.get(f'/contacts/detail/{self.contacts.pk}/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        response = self.client.delete(f'/products/delete/{self.product.pk}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
