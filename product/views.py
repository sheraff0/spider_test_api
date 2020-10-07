# from django.shortcuts import render
from rest_framework import viewsets, permissions, response
from rest_framework.generics import RetrieveAPIView
from .serializers import (
    CategorySerializer, CompanySerializer,
    ProductSerializer, DetailedProductSerializer)
from .models import Category, Company, Product


class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CompanyViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    queryset = Company.objects.filter(is_active=True)
    serializer_class = CompanySerializer


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
