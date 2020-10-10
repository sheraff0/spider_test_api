from rest_framework import serializers
from django.contrib.gis.db.models.functions import Distance
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


class GeoCompanySerializer(serializers.ModelSerializer):
    distance = serializers.SerializerMethodField('_distance')

    def _distance(self, obj):
        try:
            return round(obj.distance.m / 1000)
        except AttributeError:
            return

    class Meta:
        model = Company
        fields = [*[f.name for f in Company._meta.fields], 'distance']
