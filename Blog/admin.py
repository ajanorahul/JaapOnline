from django.contrib import admin

from .models import Product,Category,SubCategory,FeatureProduct


# Register your models here.
admin.site.register(Product)
admin.site.register(FeatureProduct)
admin.site.register(Category)
admin.site.register(SubCategory)
