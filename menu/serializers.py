from rest_framework.serializers import ModelSerializer

from .models import Category, Product


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        exclude = ['id']


class ProductSerializer(ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Product
        exclude = ['id']