from rest_framework import generics
from .models import Contact
from core import models
from .serializers import ContactSerializer

class ListContact(generics.ListCreateAPIView):
    queryset = models.Contact.objects.all()
    serializer_class = ContactSerializer


class DetailContact(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Contact.objects.all()
    serializer_class = ContactSerializer
