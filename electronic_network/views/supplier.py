from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from electronic_network.models import SupplierNode
from electronic_network.paginators import Pagination
from electronic_network.permissions import IsActiveUser
from electronic_network.serializers import SupplierSerializer
from django_filters.rest_framework import DjangoFilterBackend


class SupplierListAPIView(generics.ListAPIView):
    queryset = SupplierNode.objects.all()
    serializer_class = SupplierSerializer
    pagination_class = Pagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ('contacts__country',)

    permission_classes = [IsAuthenticated, IsActiveUser]


class SupplierCreateAPIView(generics.CreateAPIView):
    serializer_class = SupplierSerializer
    permission_classes = [IsAuthenticated, IsActiveUser]


class SupplierUpdateAPIView(generics.UpdateAPIView):
    queryset = SupplierNode.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = [IsAuthenticated, IsActiveUser]


class SupplierDetailAPIView(generics.RetrieveAPIView):
    queryset = SupplierNode.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = [IsAuthenticated, IsActiveUser]


class SupplierDestroyAPIView(generics.DestroyAPIView):
    queryset = SupplierNode.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = [IsAuthenticated, IsActiveUser]
