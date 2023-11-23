from django.shortcuts import render
from rest_framework import viewsets
from api.models import Invoice
from api.serializers import InvoiceSerializer
# Create your views here.


class InvoiceViewSet(viewsets.ModelViewSet):
    queryset= Invoice.objects.all()
    serializer_class= InvoiceSerializer
