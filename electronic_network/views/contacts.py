from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from electronic_network.models import Contacts
from electronic_network.paginators import Pagination
from electronic_network.permissions import IsActiveUser
from electronic_network.serializers import ContactsSerializer


class ContactsListAPIView(generics.ListAPIView):
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer
    pagination_class = Pagination

    permission_classes = [IsAuthenticated, IsActiveUser]


class ContactsCreateAPIView(generics.CreateAPIView):
    serializer_class = ContactsSerializer
    permission_classes = [IsAuthenticated, IsActiveUser]


class ContactsUpdateAPIView(generics.UpdateAPIView):
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer
    permission_classes = [IsAuthenticated, IsActiveUser]


class ContactsDetailAPIView(generics.RetrieveAPIView):
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer
    permission_classes = [IsAuthenticated, IsActiveUser]


class ContactsDestroyAPIView(generics.DestroyAPIView):
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer
    permission_classes = [IsAuthenticated, IsActiveUser]
