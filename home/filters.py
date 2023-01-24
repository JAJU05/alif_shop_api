from django_filters import rest_framework as filters, NumberFilter

from home.models import Product


class ProductFilter(filters.FilterSet):
    from_price = NumberFilter(field_name='price', lookup_expr='gte')
    to_price = NumberFilter(field_name='price', lookup_expr='lte')

    class Meta:
        model = Product
        fields = ('from_price', 'to_price', 'category__name')
