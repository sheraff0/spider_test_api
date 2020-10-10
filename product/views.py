# from django.shortcuts import render
from rest_framework import viewsets, permissions, response, status
from rest_framework.decorators import action
from .serializers import (
    CategorySerializer, CompanySerializer,
    ProductSerializer, DetailedProductSerializer,
    GeoCompanySerializer)
from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.geos import Point
from .models import Category, Company, Product


class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CompanyViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    queryset = Company.objects.filter(is_active=True)
    serializer_class = CompanySerializer

    @action(methods=['GET'], detail=False)
    def distances(self, request):
        try:
            lon = float(request.GET.get('lon'))
            lat = float(request.GET.get('lat'))
        except TypeError:
            return response.Response(
                {"detail": "Неверно заданы координаты"},
                status=status.HTTP_404_NOT_FOUND
            )
        queryset = Company.objects.annotate(
            distance=Distance('location', Point(lon, lat, srid=4326))
        ).order_by('distance')
        serializer = GeoCompanySerializer(queryset, many=True)
        return response.Response(serializer.data)


class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    queryset = Product.objects.filter(
        is_active=True, company__is_active=True)
    serializer_class = ProductSerializer
    filterset_fields = {
        'category': ['exact', ],
        'company': ['exact', ],
        'title': ['icontains', ]
    }

    def retrieve(self, request, pk):
        instance = self.get_object()
        serializer = DetailedProductSerializer(instance)
        return response.Response(serializer.data)
