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
    user_name = str(user)
    try:
        customer = Customer.objects.get(user = user)
        designation = customer.designation
    except TypeError:
        context = {
            'dish' : dish,
            'user' : user_name,
        }
        return render(request, 'menu/index.html', context=context)
    if str(customer.designation) == 'Restaurant':
        new_dish = []
        for i in dish:
            if i.restaurant == customer.user:
                new_dish.append(i)
        dish = new_dish
    context = {
        'dish': dish,
        'user': user_name,
        'designation' : str(designation),
    }
    return render(request, 'menu/index.html', context=context)


def restaurant_search(request, rest):
    dish = []
    for i in Dish.objects.all():
        restaurant = str(i.restaurant)
        if restaurant == rest:
            dish.append(i)
    user = request.user
    user = str(user)
    context = {
        'dish': dish,
        'restaurant': rest,
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
            password = request.POST['password1']
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
            messages.success(request,'Your account is created successfully.')
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


@login_required
def dish_creation(request):
    context = {
        'form' : 'dish_creation'
    }
    return render(request, 'menu/dish.html', context = context)


@login_required
def dish_modification(request):
    context = {
        'form': 'dish_modification'
    }
    return render(request, 'menu/dish.html', context=context)


@login_required
def dish_deletion(request):
    context = {
        'form': 'dish_deletion'
    }
    return render(request, 'menu/dish.html', context=context)
