from django import forms
from django.db.models.base import Model
from .models import *

class additemForm(forms.ModelForm):
  class Meta:
    model = items
    fields=['items_code','items_name']
# class additemForm(forms.ModelForm):
#     itemcode = forms.IntegerField(label='item code', max_length=1000)
#     itemname = forms.CharField(label='item name', max_length=1000)
class addcustomerForm(forms.ModelForm):
  class Meta:
    model = customer
    fields=['customer_code','customer_name','customer_mobile']

class addstorageForm(forms.ModelForm):
  class Meta:
    model = storage
    fields=['storage_code','storage_name','storage_location']

class addsupplierForm(forms.ModelForm):
  class Meta:
    model = supplier
    fields=['supplier_code','supplier_name','supplier_mobile']









