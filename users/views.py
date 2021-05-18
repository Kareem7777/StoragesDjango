from django.shortcuts import render , redirect
from django.http import HttpResponse ,HttpResponseRedirect
# from users import forms
from users import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required



def indexview(request):
    return render(request , "index.html")

@login_required
def dashboardView(request):
    return render(request , "dashboard.html")


def registerView(request):
    if request.method == "POST":

        form = UserCreationForm(request.POST)
        if form.is_valid():

            form.save()
            return redirect('login_url')
    else:
        form  = UserCreationForm()


    return render(request , "registration/register.html" , {'form':form})
