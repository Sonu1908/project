# from attr import fields
from rest_framework import serializers
from api.models import Invoice


#create serializers here 
class InvoiceSerializer(serializers.HyperlinkedModelSerializer):
    invoice_id=serializers.ReadOnlyField()
    class Meta:
        model = Invoice
        fields="__all__"




