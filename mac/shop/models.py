from django.db import models

# Create your models here.
class Product(models.Model):
    prod_id = models.AutoField
    prod_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50,default="")
    sub_category = models.CharField(max_length=50,default="")
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to='shop/images',default="")
    desc = models.CharField(max_length=200)
    pub_date = models.DateField()

    def __str__(self):
        return self.prod_name

class Query(models.Model):
    query_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50,default="")
    email = models.CharField(max_length=50,default="")
    phone = models.CharField(max_length=20,default="")
    query = models.CharField(max_length=1000,default="")

    def __str__(self):
        return self.name