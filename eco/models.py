from django.db import models

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
