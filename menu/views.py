from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *


# Create your views here.

def index(request):
    dish = Dish.objects.all()
    user = request.user
    user = str(user)
    context = {
        'dish': dish,
        'user': user
    }
    return render(request, 'menu/index.html', context=context)


def resturant_search(request, rest):
    dish = []
    for i in Dish.objects.all():
        resturant = str(i.resturant)
        if resturant == rest:
            dish.append(i)
    user = request.user
    user = str(user)
    context = {
        'dish': dish,
        'resturant': rest,
        'user': user
    }
    return render(request, 'menu/index.html', context=context)


def tag_search(request, tag):
    dish = []
    for i in Dish.objects.all():
        tags = str(i.tags)
        if tags == tag:
            dish.append(i)
    user = request.user
    user = str(user)
    context = {
        'dish': dish,
        'tag': tag,
        'user': user
    }
    return render(request, 'menu/index.html', context=context)


def user_creation(request):
    form = UserCreationForm
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            login(request, user)
        return redirect('customer_creation')
    context = {
        'form': form,
    }
    return render(request, 'menu/customer_creation.html', context=context)


@login_required
def customer_creation(request):
    form = Customer_form
    if request.method == 'POST':
        form = Customer_form(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            user = User.objects.get(username=request.user)
            form.user = user
            form.save()
            messages.success('Your account is created successfully.')
        return redirect('index')
    context = {
        'form': form,
    }

    return render(request, 'menu/customer_creation.html', context=context)


def log_out(request):
    logout(request)
    messages.success(request, 'You are successfully logged out')
    return redirect('index')


def log_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'user not exits')
            return redirect('log_in')

        user = authenticate(request, username=username, password=password)

        if user:
            messages.success(request, 'login successfully')
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'username or password is incorrect')
            return redirect('log_in')
    return render(request, 'menu/log_in.html')
