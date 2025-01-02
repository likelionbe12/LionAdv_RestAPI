from rest_framework import serializers
from .models import Product

# 예전에 배운 Form과 비교해서 생각해보면 쉽습니다.
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name','description','price','in_stock']