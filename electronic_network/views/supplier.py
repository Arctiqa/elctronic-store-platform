from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from electronic_network.models import SupplierNode
from electronic_network.serializers import SupplierSerializer


class SupplierListAPIView(generics.ListAPIView):
    queryset = SupplierNode.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = [IsAuthenticated]


class SupplierCreateAPIView(generics.CreateAPIView):
    serializer_class = SupplierSerializer
    permission_classes = [IsAuthenticated]


class SupplierUpdateAPIView(generics.UpdateAPIView):
    queryset = SupplierNode.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = [IsAuthenticated]


class SupplierDetailAPIView(generics.RetrieveAPIView):
    queryset = SupplierNode.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = [IsAuthenticated]


class SupplierDestroyAPIView(generics.DestroyAPIView):
    queryset = SupplierNode.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = [IsAuthenticated]
