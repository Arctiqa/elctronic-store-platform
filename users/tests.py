from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from electronic_network.models import SupplierNode
from users.models import User


class ElectronicNetworkTestCase(APITestCase):
    def SetUp(self):
        self.client = APIClient()
        self.user = User.objects.create(
            email='test@test.test',
            password='test',
            is_active=True,
        )

        self.client.force_authenticate(user=self.user)

        self.supplier = SupplierNode.objects.create(

        )