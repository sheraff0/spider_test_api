from rest_framework import routers
from product.views import (
    CategoryViewSet, CompanyViewSet, ProductViewSet)

router = routers.DefaultRouter()

router.register('categories', CategoryViewSet)
router.register('companies', CompanyViewSet)
router.register('products', ProductViewSet)
