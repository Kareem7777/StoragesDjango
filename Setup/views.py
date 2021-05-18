from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from Setup import models as setupmodel
from .forms import *
from Transaction import models as transactionmodel


from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def home(request):
    page_title = 'Setup Home Page'
    return render(request, 'setup.html', {'page_title': page_title})


def item(request):

    aa = setupmodel.items.objects.all()
    # aa = setupmodel.objects.raw('SELECT * FROM Setup_items')
    page_title = 'Items Data'

    return render(request, 'item.html', {'data': aa, 'page_title': page_title})


def supplier(request):
    aa = setupmodel.supplier.objects.all()
    page_title = 'Suppliers Data'
    return render(request, 'supplier.html', {'data': aa, 'page_title': page_title})


def customer(request):
    aa = setupmodel.customer.objects.all()
    page_title = 'Customers Data'

    return render(request, 'customer.html', {'data': aa, 'page_title': page_title})


def storage(request):
    aa = setupmodel.storage.objects.all()
    page_title = 'Storages Data'

    return render(request, 'storage.html', {'data': aa, 'page_title': page_title})


def additem(request):
    page_title = 'Add Item'
    submitted = False
    if request.method == 'POST':
        newitem = additemForm(request.POST or None)
        if newitem.is_valid():
            newitem.save()
        return HttpResponseRedirect('/Setup/additem?submitted=True')
    else:
        newitem = additemForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'additems.html', {'page_title':page_title, 'submitted': submitted})


def addstorage(request):
    page_title = 'Add Storage'
    submitted = False
    if request.method == 'POST':
        newstorage = addstorageForm(request.POST or None)
        if newstorage.is_valid():
            newstorage.save()
        return HttpResponseRedirect('/Setup/addstorage?submitted=True')
    else:
        newstorage = addstorageForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'addstorage.html', {'page_title':page_title, 'submitted': submitted})


def addcustomer(request):
    page_title = 'Add Customer'
    submitted = False
    if request.method == 'POST':
        newcustomer = addcustomerForm(request.POST or None)
        if newcustomer.is_valid():
            newcustomer.save()
        return HttpResponseRedirect('/Setup/addcustomer?submitted=True')
    else:
        newcustomer = addcustomerForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'addcustomer.html', {'page_title':page_title, 'submitted': submitted})


def addsupplier(request):
    page_title = 'Add Supplier'
    submitted = False
    if request.method == 'POST':
        newsupplier = addsupplierForm(request.POST or None)
        if newsupplier.is_valid():
            newsupplier.save()
        return HttpResponseRedirect('/Setup/addsupplier?submitted=True')
    else:
        newsupplier = addsupplierForm
        if 'submitted' in request.GET:
            submitted = True
        return render(request, 'addsupplier.html', {'page_title':page_title, 'submitted': submitted})
