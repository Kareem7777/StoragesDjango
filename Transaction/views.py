from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from Transaction.models import *
from Transaction.forms import *
from Setup.models import *
# Create your views here.


def transaction_fun(request):
    return HttpResponse('Hello from transaction function')


def master_in_fun(request):
    aa = master_in.objects.all()
    ss = detail_in.objects.all()
    page_title = 'Master In Data'
    return render(request, 'in.html',  {'data': aa, 'zata': ss, 'page_title': page_title})


def master_out_fun(request):
    aa = master_out.objects.all()
    ss = detail_out.objects.all()
    page_title = 'Master Out Data'
    return render(request, 'out.html',  {'data': aa, 'zata': ss, 'page_title': page_title})


def addmaster_in(request):
    page_title = 'Add Master In'
    aa = master_in.objects.all()
    ss = storage.objects.all()
    pp = supplier.objects.all()
    cc = customer.objects.all()
    ii = items.objects.all()
    submitted = False
    if request.method == 'POST':
        newmaster_in = addmaster_inForm(request.POST)

        if newmaster_in.is_valid():
            newmaster_in.save()
        return HttpResponseRedirect('/Transaction/addmaster_in?submitted=True')
    else:
        newmaster_in = addmaster_inForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'addmaster_in.html', {'page_title':page_title,'data': aa, 'item_data': ii, 'storage_data': ss, 'customer_data': cc, 'supplier_data': pp, 'submitted': submitted})


def addmaster_out(request):
    page_title = 'Add Master Out'
    aa = master_out.objects.all()
    ss = storage.objects.all()
    pp = supplier.objects.all()
    cc = customer.objects.all()
    submitted = False
    if request.method == 'POST':
        newmaster_out = addmaster_outForm(request.POST or None)

        if newmaster_out.is_valid():
            newmaster_out.save()
        return HttpResponseRedirect('/Transaction/addmaster_out?submitted=True')
    else:
        newmaster_out = addmaster_outForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'addmaster_out.html', {'page_title':page_title,'data': aa, 'storage_data': ss, 'customer_data': cc, 'supplier_data': pp, 'submitted': submitted})


def adddetail_in(request):
    page_title = 'Add Detail In'
    mm = master_in.objects.all()
    aa = detail_in.objects.all()
    ii = items.objects.all()
    submitted = False
    if request.method == 'POST':
        newdetail_in = adddetail_inForm(request.POST or None)

        if newdetail_in.is_valid():
            newdetail_in.save()
        return HttpResponseRedirect('/Transaction/adddetail_in?submitted=True')
    else:
        newdetail_in = adddetail_inForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'adddetail_in.html', {'page_title':page_title,'detail_in_data': aa, 'item_data': ii, 'master_in_data': mm, 'submitted': submitted})


def adddetail_out(request):
    page_title = 'Add Detail Out'
    mm = master_out.objects.all()
    aa = detail_out.objects.all()
    ii = items.objects.all()
    submitted = False
    if request.method == 'POST':
        newdetail_out = adddetail_outForm(request.POST or None)

        if newdetail_out.is_valid():
            newdetail_out.save()
        return HttpResponseRedirect('/Transaction/adddetail_out?submitted=True')
    else:
        newdetail_out = adddetail_outForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'adddetail_out.html', {'page_title':page_title,'detail_out_data': aa, 'item_data': ii, 'master_out_data': mm, 'submitted': submitted})


def detail_in_fun(request, foreign_master_in_id):
    page_title = 'Detail In Data'
    aa = master_in.objects.get(master_in_id=foreign_master_in_id)
    bb = detail_in.objects.filter(Master_in_id=foreign_master_in_id)
    return render(request, 'detail_in.html', {'page_title':page_title,'data': aa, 'zata': bb})


def detail_out_fun(request, foreign_master_out_id):
    page_title = 'Detail Out Data'
    aa = master_out.objects.get(master_out_id=foreign_master_out_id)
    bb = detail_out.objects.filter(Master_out_id=foreign_master_out_id)
    return render(request, 'detail_out.html', {'page_title':page_title,'data': aa, 'zata': bb})


# def item_report(request, the_item):
#     item_data = items.objects.get(items_id=the_item)
#     detail_in_data = detail_in.objects.filter(Items_id=the_item)
#     detail_out_data = detail_out.objects.filter(Items_id=the_item)
#     bbb = 0
#     ddd = 0
#     page_title = 'Item Report'
#     for i in detail_in_data:
#         sumin = i.detail_in_quantity
#         bbb += sumin
#     for u in detail_out_data:
#         sumout = u.detail_out_quantity
#         ddd += sumout
#     sumtot = bbb - ddd
#     return render(request, 'itemreport.html', {'item_data': item_data,
#                                                'detail_in_data': detail_in_data, 'detail_out_data': detail_out_data,
#                                                'sumin': bbb, 'sumout': ddd, 'sumtot': sumtot, 'page_title': page_title})

# def supplier_report(request,the_supplier):
#     page_title='Supplier Report'
#     sumin = 0
#     sumout = 0
#     supplier_data = supplier.objects.get(supplier_id= the_supplier)
#     master_in_data = master_in.objects.filter(Supplier_id=the_supplier)
#     master_out_data = master_out.objects.filter(Supplier_id=the_supplier)
#     for mi in master_in_data:
#         the_master_in = mi.master_in_id
#         detail_in_data = detail_in.objects.filter(Master_in_id=the_master_in)
#         for di in detail_in_data:
#             bb  = (di.detail_in_quantity)*(di.detail_in_price)
#             sumin +=bb
#     for mo in master_out_data:
#         the_master_out = mo.master_out_id
#         detail_out_data = detail_out.objects.filter(Master_out_id = the_master_out)
#         for do in detail_out_data:
#             tt = (do.detail_out_quantity)*(do.detail_out_price)
#             sumout+=tt
#     sumtot = sumin-sumout
#     return render (request, 'supplierreport.html',{'supplier_data':supplier_data,'detail_in_data':detail_in_data,
#     'page_title':page_title,'sumtot':f"{sumtot:,}"})


def try_in(request):
    aa = master_in.objects.all()
    ss = storage.objects.all()
    pp = supplier.objects.all()
    cc = customer.objects.all()
    #submitted= False
    if request.method == 'POST':
        newmaster_in = addmaster_inForm(request.POST or None)

        if newmaster_in.is_valid():
            newmaster_in.save()
        # return HttpResponseRedirect ('/Transaction/addmaster_in?submitted=True')
    else:
        newmaster_in = addmaster_inForm
        # if 'submitted' in request.GET:
        #     submitted= True
    return render(request, 'out2.html', {'data': aa, 'storage_data': ss, 'customer_data': cc, 'supplier_data': pp})


def tryde_in(request, foreign_master_in_id):
    mm = master_in.objects.get(master_in_id=foreign_master_in_id)
    dd = detail_in.objects.all()
    ii = items.objects.all()
    if request.method == 'POST':
        newdetail_in = adddetail_inForm(request.POST)

        if newdetail_in.is_valid():
            newdetail_in.save()
        # return HttpResponseRedirect ('/Transaction/adddetail_in?submitted=True')
    else:
        newdetail_in = adddetail_inForm
    return render(request, 'try1.html', {'data': dd, 'mata': mm, 'iata': ii})


def cash_in_view(request):  # nod finished
    page_title = 'Cash Out'
    mm = cash_in.objects.all()
    oo = customer.objects.all()
    ii = supplier.objects.all()
    submitted = False
    if request.method == 'POST':
        addcash_inval = addcash_inForm(request.POST or None)

        if addcash_inval.is_valid():
            addcash_inval.save()
        # return HttpResponseRedirect ('/Transaction/adddetail_in?submitted=True') #nod finished
    else:
        addcash_inval = addcash_inForm
        if 'submitted' in request.GET:
            submitted = True
    # nod finished
    return render(request, 'cash_in_view.html', {'page_title':page_title,'oata': oo, 'iata': ii, 'mata': mm, 'submitted': submitted})


def suppliers_report(request):
    page_title = 'Suppliers Report'
    ss = supplier.objects.all()
    tot = []
    for i in ss:
        sum_in = 0
        sum_out = 0
        total = 0
        the_supplier = i.supplier_id
        mi = master_in.objects.filter(Supplier_id=the_supplier)
        for ii in mi:
            the_master_in = ii.master_in_id
            di = detail_in.objects.filter(Master_in_id=the_master_in)
            for iii in di:
                bi = (iii.detail_in_price)*(iii.detail_in_quantity)
                sum_in += bi
        mo = master_out.objects.filter(Supplier_id=the_supplier)
        for oo in mo:
            the_master_out = oo.master_out_id
            do = detail_out.objects.filter(Master_out_id=the_master_out)
            for ooo in do:
                bo = (ooo.detail_out_price)*(ooo.detail_out_quantity)
                sum_out += bo
        total = sum_in - sum_out
        total = f"{total:,}"
        tot.append(total)
    my_list = zip(tot, ss)

    args = {'page_title': page_title, 'my_list': my_list}
    return render(request, 'suppliers_report.html', args)


def customers_report(request):
    page_title = 'customers Report'
    ss = customer.objects.all()
    tot = []
    for i in ss:
        sum_in = 0
        sum_out = 0
        total = 0
        the_customer = i.customer_id
        mi = master_in.objects.filter(Customer_id=the_customer)
        for ii in mi:
            the_master_in = ii.master_in_id
            di = detail_in.objects.filter(Master_in_id=the_master_in)
            for iii in di:
                bi = (iii.detail_in_price)*(iii.detail_in_quantity)
                sum_in += bi
        mo = master_out.objects.filter(Customer_id=the_customer)
        for oo in mo:
            the_master_out = oo.master_out_id
            do = detail_out.objects.filter(Master_out_id=the_master_out)
            for ooo in do:
                bo = (ooo.detail_out_price)*(ooo.detail_out_quantity)
                sum_out += bo
        total = sum_in - sum_out
        total = f"{total:,}"
        tot.append(total)
    my_list = zip(tot, ss)

    args = {'page_title': page_title, 'my_list': my_list}
    return render(request, 'customers_report.html', args)


def items_report(request):
    page_title = 'Items Report'
    ii = items.objects.all()
    total = []
    for i in ii:
        total_quantity = 0
        tot_quantity_in = 0
        tot_quantity_out = 0
        the_item = i.items_id
        di = detail_in.objects.filter(Items_id=the_item)
        do = detail_out.objects.filter(Items_id=the_item)
        for dii in di:
            quantity_in = dii.detail_in_quantity
            tot_quantity_in += quantity_in
        for doo in do:
            quantity_out = doo.detail_out_quantity
            tot_quantity_out += quantity_out
        total_quantity = tot_quantity_in - tot_quantity_out
        total.append(total_quantity)
    my_list = zip(ii, total)
    args = {'page_title': page_title, 'my_list': my_list}
    return render(request, 'items_report.html', args)
