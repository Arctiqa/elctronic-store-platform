from rest_framework import serializers

from electronic_network.models import SupplierNode, Product


class NodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupplierNode
        fields = ('id', 'name', 'type', 'email', 'country', 'city', 'supplier', 'house_number', 'debts')


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('node', 'name', 'model', 'release_date')
