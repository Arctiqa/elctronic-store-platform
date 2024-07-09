from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated

from electronic_network.models import Contacts
from electronic_network.serializers import ContactsSerializer


class ContactsListAPIView(generics.ListAPIView):
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer
    permission_classes = [IsAuthenticated]


class ContactsCreateAPIView(generics.CreateAPIView):
    serializer_class = ContactsSerializer
    permission_classes = [IsAuthenticated]


class ContactsUpdateAPIView(generics.UpdateAPIView):
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer
    permission_classes = [IsAuthenticated]


class ContactsDetailAPIView(generics.RetrieveAPIView):
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer
    permission_classes = [IsAuthenticated]


class ContactsDestroyAPIView(generics.DestroyAPIView):
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer
    permission_classes = [IsAuthenticated]
