from django.db import models

class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    cost = models.FloatField()
    category = models.CharField(max_length=100)
    name = models.CharField(max_length=200)
    brand = models.CharField(max_length=100)
    retail_price = models.FloatField()
    department = models.CharField(max_length=100)
    sku = models.CharField(max_length=100)
    distribution_center_id = models.IntegerField()

    def __str__(self):
        return self.name
