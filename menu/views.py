from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from . models import * 
from .forms import *


# Create your views here.

def index(request):
    dish = Dish.objects.all()
    context = {
        'dish' : dish
    }
    return render(request, 'menu/index.html', context = context)

def resturant_search(request, rest):
    dish = []
    for i in Dish.objects.all():
        resturant = str(i.resturant)
        if resturant == rest:
            dish.append(i)
    context = {
        'dish' : dish,
        'resturant' : rest
    }
    return render(request, 'menu/index.html', context = context)


def tag_search(request, tag):
    dish = []
    for i in Dish.objects.all():
        tags = str(i.tags)
        if tags == tag:
            dish.append(i)
    context = {
        'dish' : dish,
        'tag' : tag
    }
    return render(request, 'menu/index.html', context = context)

def user_creation(request):
    form = UserCreationForm
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST['username']
            password = request.POST['password1']
            user = authenticate(request, username = username, password = password)
            login(request, user)
        return redirect('customer_creation')
    context = {
        'form' : form,
    }
    return render(request, 'menu/customer_creation', context = context)

@login_required
def customer_creation(request):
    form = Customer_form
    if request.method == 'POST':
        form = Customer_form(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            user = User.objects.get(username = request.user)
            form.user = user
            form.save()
        return redirect('index')
    context = {
        'form' : form,
    }

    return render(request, 'menu/customer_creation', context = context)