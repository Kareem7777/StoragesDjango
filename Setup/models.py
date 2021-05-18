from django.db import models
# Create your models here.


class items(models.Model):
    items_id = models.AutoField(primary_key=True)
    items_code = models.IntegerField(blank=True, null=True,unique=True)
    items_name = models.CharField(max_length=100)


class storage(models.Model):
    storage_id = models.AutoField(primary_key=True)
    storage_code = models.IntegerField(blank=True, null=True,unique=True)
    storage_name = models.CharField(max_length=100)
    storage_location = models.CharField(max_length=400)


class customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_code = models.IntegerField(blank=True, null=True,unique=True)
    customer_name = models.CharField(max_length=100)
    customer_mobile = models.CharField(max_length=100)


class supplier(models.Model):
    supplier_id = models.AutoField(primary_key=True)
    supplier_code = models.IntegerField(blank=True, null=True,unique=True)
    supplier_name = models.CharField(max_length=100)
    supplier_mobile = models.CharField(max_length=100)
