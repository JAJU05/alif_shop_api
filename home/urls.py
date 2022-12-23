from django.urls import path, include
from rest_framework.routers import DefaultRouter

from home.views import ProductModelViewSet, CategoryModelViewSet, ShopModelViewSet, ProductImagesModelViewSet

router = DefaultRouter()
router.register('product', ProductModelViewSet, 'product')
router.register('category', CategoryModelViewSet, 'category')
router.register('shop', ShopModelViewSet, 'shop')
router.register('product_images', ProductImagesModelViewSet, 'product-images')

urlpatterns = [
    path('', include(router.urls)),
]
