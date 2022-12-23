from django.contrib import admin

# Register your models here.
from home.models import Category, ProductImages, Product, Shop

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductImages)
admin.site.register(Shop)