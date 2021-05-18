from django.db import models
from django.db.models.deletion import CASCADE
from Setup.models import *
# Create your models here.


class master_in(models.Model):
    master_in_id = models.AutoField(primary_key=True)
    master_in_code = models.IntegerField(blank=True, null=True)
    master_in_date = models.DateField(auto_now_add=True)
    master_in_movenumber = models.IntegerField(blank=True, null=True)
    master_in_notes = models.CharField(max_length=1000)
    Supplier_id = models.ForeignKey(
        supplier, on_delete=models.CASCADE, default=1, null=True)
    Storage_id = models.ForeignKey(
        storage, on_delete=models.CASCADE, default=1, null=True)
    Customer_id = models.ForeignKey(
        customer, on_delete=models.CASCADE, default=1, null=True)


class detail_in(models.Model):
    detail_in_id = models.AutoField(primary_key=True)
    detail_in_code = models.IntegerField(blank=True, null=True)
    detail_in_quantity = models.IntegerField(blank=True, null=True)
    detail_in_price = models.FloatField()
    Items_id = models.ForeignKey(
        items, on_delete=models.CASCADE, default=1)
    Master_in_id = models.ForeignKey(
        master_in, on_delete=models.CASCADE, default=1)


class master_out(models.Model):
    master_out_id = models.AutoField(primary_key=True)
    master_out_code = models.IntegerField(blank=True, null=True)
    master_out_date = models.DateField(auto_now_add=True)
    master_out_movenumber = models.IntegerField(blank=True, null=True)
    master_out_notes = models.CharField(max_length=1000)
    Supplier_id = models.ForeignKey(
        supplier, on_delete=models.CASCADE, default=1)
    Storage_id = models.ForeignKey(
        storage, on_delete=models.CASCADE, default=1)
    Customer_id = models.ForeignKey(
        customer, on_delete=models.CASCADE, default=1)


class detail_out(models.Model):
    detail_out_id = models.AutoField(primary_key=True)
    detail_out_code = models.IntegerField(blank=True, null=True)
    detail_out_quantity = models.IntegerField(blank=True, null=True)
    detail_out_price = models.FloatField()
    Items_id = models.ForeignKey(
        items, on_delete=models.CASCADE, default=1)
    Master_out_id = models.ForeignKey(
        master_out, on_delete=models.CASCADE, default=1)


class cash_in(models.Model):
    cash_in_id = models.AutoField(primary_key=True)
    cash_in_code = models.IntegerField(blank=True)
    cash_in_date = models.DateField(auto_now_add=True)
    cash_in_notes = models.CharField(max_length=1000, blank=True, null=True)
    cash_in_paid = models.FloatField(blank=True, null=True)
    Customer_id = models.ForeignKey(
        customer, on_delete=models.CASCADE, null=True)
    Supplier_id = models.ForeignKey(
        supplier, on_delete=models.CASCADE, null=True)
