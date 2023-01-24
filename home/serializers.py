from django_elasticsearch_dsl_drf.serializers import DocumentSerializer
from rest_framework.serializers import ModelSerializer

from home.documents import ProductDocument
from home.models import Product, Shop, ProductImages, Category


class ProductModelSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class CategoryModelSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ShopModelSerializer(ModelSerializer):
    class Meta:
        model = Shop
        fields = '__all__'


class ProductImagesModelSerializer(ModelSerializer):
    class Meta:
        model = ProductImages
        fields = '__all__'


class ProductDocumentSerializer(DocumentSerializer):
    class Meta:
        document = ProductDocument
        fields = [
            'name',
            'description', 'category__name'
        ]
