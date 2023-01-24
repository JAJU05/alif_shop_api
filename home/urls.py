from django.urls import path, include
from rest_framework.routers import DefaultRouter

from home.views import ProductModelViewSet, CategoryModelViewSet, ShopModelViewSet, ProductImagesModelViewSet, \
    ProductDocumentViewSet

router = DefaultRouter()
# router.register('products', ProductModelViewSet, 'products')
router.register('category', CategoryModelViewSet, 'category')
router.register('shop', ShopModelViewSet, 'shop')
router.register('product_images', ProductImagesModelViewSet, 'product-images')
router.register('product', ProductDocumentViewSet, 'product')

urlpatterns = [
    path('', include(router.urls)),
]
