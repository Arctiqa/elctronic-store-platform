from rest_framework import serializers

from electronic_network.models import SupplierNode, Product, Contacts


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('supplier', 'name', 'model', 'release_date')


class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = ('supplier', 'email', 'country', 'city', 'street', 'house')


class SupplierSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)
    contacts = ContactsSerializer(many=True, read_only=True)

    class Meta:
        model = SupplierNode
        fields = ('id', 'name', 'type', 'supplier', 'debts', 'hierarchy_level', 'products', 'contacts')
