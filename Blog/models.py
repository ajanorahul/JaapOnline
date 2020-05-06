from django.db import models
from django.conf import settings
from django.shortcuts import reverse

# Create your models here.





class Product(models.Model):
    category = models.CharField(max_length=100)
    sub_category = models.CharField(max_length=100, default="")
    name = models.CharField(max_length=100)
    dest = models.TextField()
    img = models.ImageField(upload_to ='pics')
    price = models.IntegerField()
    time = models.TimeField()
    offer = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Category(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length =150)
    status = models.IntegerField()
    create_at =models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.title


class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete =models.CASCADE)
    sub_category = models.CharField(max_length=100)

    def __str__(self):
        return self.sub_category

class FeatureProduct(models.Model):
    category = models.ForeignKey(Category, on_delete =models.CASCADE)
    sub_category = models.ForeignKey(SubCategory, on_delete =models.CASCADE)
    title = models.CharField(max_length=150)
    price = models.IntegerField()
    description = models.TextField()
    img = models.ImageField(upload_to ='pics2')

    def __str__(self):
        return self.title
