from django.db import models

# Create your models here.
class Product(models.Model):
    prod_name = models.CharField(max_length=255, null=False, blank=False)
    prod_desc = models.TextField(null=False, blank=False)
    prod_price = models.FloatField(null=False, blank=False)
    prod_image = models.ImageField(upload_to='images/product/',default='images/no_product_image.png')
    is_deleted = models.BooleanField(default=False)