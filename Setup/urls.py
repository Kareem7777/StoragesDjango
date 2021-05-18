from django.urls import path
from Setup.views import *


urlpatterns = [

    path('home', home, name='home-page'),
    path('item', item, name='item-data'),
    path('supplier', supplier, name='supplier-data'),
    path('customer', customer, name='customer-data'),
    path('storage', storage, name='storage-data'),
    path('additem', additem , name = 'add-item'),
    path('addcustomer', addcustomer, name = 'add-customer'),
    path('addstorage', addstorage, name = 'add-storage'),
    path('addsupplier', addsupplier, name = 'add-supplier'),


]
