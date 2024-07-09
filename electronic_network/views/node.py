from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated

from electronic_network.models import SupplierNode
from electronic_network.serializers import NodeSerializer


class NodeListAPIView(generics.ListAPIView):
    queryset = SupplierNode.objects.all()
    serializer_class = NodeSerializer
    permission_classes = [IsAuthenticated]


class NodeCreateAPIView(generics.CreateAPIView):
    serializer_class = NodeSerializer
    permission_classes = [IsAuthenticated]


class NodeUpdateAPIView(generics.UpdateAPIView):
    queryset = SupplierNode.objects.all()
    serializer_class = NodeSerializer
    permission_classes = [IsAuthenticated]


class NodeDetailAPIView(generics.RetrieveAPIView):
    queryset = SupplierNode.objects.all()
    serializer_class = NodeSerializer
    permission_classes = [IsAuthenticated]


class NodeDestroyAPIView(generics.DestroyAPIView):
    queryset = SupplierNode.objects.all()
    serializer_class = NodeSerializer
    permission_classes = [IsAuthenticated]
