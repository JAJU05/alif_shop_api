from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry

from home.models import Product, Category


@registry.register_document
class ProductDocument(Document):
    category = fields.ObjectField(properties={
        'name': fields.TextField(),
    })

    class Index:
        name = 'products'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0,
        }

    class Django:
        model = Product
        fields = [
            'name',
            'description',
        ]

    def get_queryset(self):
        return super().get_queryset().select_related('category')

    def get_instances_from_related(self, related_instance):
        if isinstance(related_instance, Category):
            return related_instance.product_set.all()
