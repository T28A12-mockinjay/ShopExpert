from django.contrib import admin

# Register your models here.

from .models import Product, Query

admin.site.register(Product)
admin.site.register(Query)