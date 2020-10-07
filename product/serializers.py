from rest_framework import serializers
from .models import Category, Company, Product


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'


class DetailedProductSerializer(ProductSerializer):
    category = CategorySerializer(read_only=True)
    company = CompanySerializer(read_only=True)
