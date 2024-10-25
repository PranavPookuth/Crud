from rest_framework import serializers
from .models import Products

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'
class ProductsSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['product_name']