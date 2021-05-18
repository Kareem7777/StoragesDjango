from django import forms
from Transaction.models import *


class addmaster_inForm(forms.ModelForm):
    class Meta:
        model = master_in
        fields = ['master_in_code', 'master_in_movenumber',
                  'master_in_notes', 'Storage_id', 'Customer_id', 'Supplier_id']
# class additemForm(forms.ModelForm):
#     itemcode = forms.IntegerField(label='item code', max_length=1000)
#     itemname = forms.CharField(label='item name', max_length=1000)


class adddetail_inForm(forms.ModelForm):
    class Meta:
        model = detail_in
        fields = ['detail_in_code', 'detail_in_quantity',
                  'detail_in_price', 'Items_id', 'Master_in_id']


class addmaster_outForm(forms.ModelForm):
    class Meta:
        model = master_out
        fields = ['master_out_code', 'master_out_movenumber',
                  'master_out_notes', 'Storage_id', 'Customer_id', 'Supplier_id']


class adddetail_outForm(forms.ModelForm):
    class Meta:
        model = detail_out
        fields = ['detail_out_code', 'detail_out_quantity',
                  'detail_out_price', 'Items_id', 'Master_out_id']


class addcash_inForm(forms.ModelForm):
    class Meta:
        model = cash_in
        fields = ['cash_in_code','cash_in_notes',
                  'cash_in_paid', 'Customer_id', 'Supplier_id']

                  

