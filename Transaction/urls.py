from django.urls import path
from Transaction.views import *


urlpatterns = [

    path('transaction', transaction_fun),
    path('in', master_in_fun, name = 'master-in-data'),
    path('out',master_out_fun, name = 'master-out-data'),
    path('addmaster_in',addmaster_in ,name='add-master-in'),
    path('addmaster_out',addmaster_out, name='add-master-out'),
    path('adddetail_in',adddetail_in, name='add-detail-in'),
    path('adddetail_out',adddetail_out, name='add-detail-out'),
    path('detail_in/<foreign_master_in_id>',detail_in_fun, name='detail-in'),
    path('detail_out/<foreign_master_out_id>',detail_out_fun, name='detail-out'),
    # path('item_report/<the_item>', item_report, name='item-report'),
    #path('supplier_report/<the_supplier>',supplier_report,name='supplier-report'),
    path('try_in',try_in,name='try-in'),
    path('tryde_in/<foreign_master_in_id>',tryde_in,name='tryde-in'),
    path('cash_in_view',cash_in_view,name='cash_in_view'),
    path('suppliers_report',suppliers_report,name='suppliers-report'),
    path('customers_report',customers_report,name='customers-report'),
    path('items_report',items_report,name='items-report'),
]
