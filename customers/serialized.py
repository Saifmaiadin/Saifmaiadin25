# customers/serializers.py
from rest_framework import serializers
from .models import Customer, CustomerContactPerson, CustomerProduct, CustomerService

class CustomerContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerContactPerson
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):
    contacts = CustomerContactSerializer(many=True, read_only=True)
    
    class Meta:
        model = Customer
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')

class CustomerProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerProduct
        fields = '__all__'

class CustomerServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerService
        fields = '__all__'