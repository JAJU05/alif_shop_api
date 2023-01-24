from django_elasticsearch_dsl_drf.filter_backends import SearchFilterBackend, FunctionalSuggesterFilterBackend
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.parsers import MultiPartParser

from rest_framework.viewsets import ModelViewSet

from home.documents import ProductDocument
# from home.filters import ProductFilter
from home.models import Product, Category, Shop, ProductImages
from home.serializers import ProductModelSerializer, CategoryModelSerializer, ShopModelSerializer, \
    ProductImagesModelSerializer, ProductDocumentSerializer


class ProductModelViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer
    # filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter,)
    # filterset_class = ProductFilter
    # search_fields = ['name']
    # ordering_fields = ['price']


class CategoryModelViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer


class ShopModelViewSet(ModelViewSet):
    queryset = Shop.objects.all()
    parser_classes = (MultiPartParser,)
    serializer_class = ShopModelSerializer


class ProductImagesModelViewSet(ModelViewSet):
    queryset = ProductImages.objects.all()
    serializer_class = ProductImagesModelSerializer


class ProductDocumentViewSet(DocumentViewSet):
    document = ProductDocument
    filter_backends = [SearchFilterBackend]
    serializer_class = ProductDocumentSerializer
    search_fields = ('name', 'description', 'category__name')
