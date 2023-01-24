import uuid

from django.db.models import Model, ForeignKey, CharField, ImageField, UUIDField, CASCADE, DecimalField, SET_NULL, \
    TextField
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class Category(MPTTModel):
    id = UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    name = CharField(max_length=55)
    parent = TreeForeignKey('self', SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name


class Shop(Model):
    id = UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    name = CharField(max_length=255)
    description = TextField()
    image = ImageField(upload_to='shops')

    def __str__(self):
        return self.name


class Product(Model):
    id = UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    name = CharField(max_length=55)
    description = TextField()
    price = DecimalField(max_digits=9, decimal_places=2)
    category = ForeignKey('home.Category', CASCADE)
    shop = ForeignKey('home.Shop', CASCADE)

    def __str__(self):
        return self.name


class ProductImages(Model):
    id = UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    images = ImageField(upload_to='adverts/images/')
    product = ForeignKey('home.Product', CASCADE)


