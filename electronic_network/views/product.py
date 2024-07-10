from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from electronic_network.models import Product
from electronic_network.paginators import Pagination
from electronic_network.permissions import IsActiveUser
from electronic_network.serializers import ProductSerializer


class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = Pagination

    permission_classes = [IsAuthenticated, IsActiveUser]


class ProductCreateAPIView(generics.CreateAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, IsActiveUser]


class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, IsActiveUser]


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, IsActiveUser]


class ProductDestroyAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, IsActiveUser]
