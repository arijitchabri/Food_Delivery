from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Tags, Dish, Designation, Customer
from .forms import *


# Create your views here.
# Index handles the landing page.
def index(request):
    dish = Dish.objects.all()   # Collecting all the dishes.
    user = request.user         # Collecting the requested user.
    user_name = str(user)       # Logged in users name as string.
    try:
        customer = Customer.objects.get(user = user)    # Collecting the customer.
        designation = str(customer.designation)         # Designation of logged in customer.
    except TypeError:           # If its an anonymous user the he will have no designation.
        context = {
            'dish' : dish,          # All available dishes.
            'user' : user_name,     # Logged in user's name as a string.
        }
        return render(request, 'menu/index.html', context=context)

    #  For general user all the dishes will show.
    # If the requested user is a Restaurant then only its menu will appear.

    if designation == 'Restaurant':
        dish = Dish.objects.filter(restaurant = user)
    context = {
        'dish': dish,                       # All the viewable dishes.
        'user': user_name,                  # Logged in user's name as a string.
        'designation' : designation,        # Designation of the user.
    }
    print(designation, type(designation))
    return render(request, 'menu/index.html', context=context)


def restaurant_search(request, rest):
    # Filtering through specific restaurant.

    restaurant = User.objects.get(username=rest)            # Collecting the restaurant.
    dish = Dish.objects.filter(restaurant = restaurant)     # Filtering the dishes.
    user = request.user
    user_name = str(user)
    context = {
        'dish': dish,
        'restaurant': rest,
        'user': user_name,
    }
    return render(request, 'menu/index.html', context=context)


def tag_search(request, tag):
    # Filtering through tag.
    tag = Tags.objects.get(tag = tag)
    dish = Dish.objects.filter(tags = tag)
    user = request.user
    user_name = str(user)
    try:
        customer = Customer.objects.get(user = user)    # Collecting the customer.
        designation = str(customer.designation)         # Designation of logged in customer.
    except TypeError:           # If its an anonymous user the he will have no designation.
        context = {
            'dish' : dish,          # All available dishes.
            'user' : user_name,     # Logged in user's name as a string.
        }
        return render(request, 'menu/index.html', context=context)
    if designation == 'Restaurant':
        # If the designation is resturant then it will filter all the dishes of that restaurant with the same tag.
        dish = Dish.objects.filter(restaurant = user, tags = tag)
    context = {
        'dish': dish,
        'tag': tag,
        'user': user_name,
        'designation' : designation,
    }
    return render(request, 'menu/index.html', context=context)

@login_required
def dish_creation(request):
    form = Dish_creation_Form
    user = request.user
    if request.method == 'POST':
        form = Dish_creation_Form(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.restaurant = user
            form.save()
            messages.success(request, 'Dish added successfully.')
            return redirect('index')
    context = {
        'form_type' : 'dish_creation',
        'form' : form
    }
    return render(request, 'menu/dish.html', context = context)


@login_required
def dish_modification(request, dish_id):
    dish = Dish.objects.get(id = dish_id)
    user = request.user
    restaurant = user
    form = Dish_creation_Form(instance=dish)
    if str(restaurant) == str(dish.restaurant):
        if request.method == 'POST':
            form = Dish_creation_Form(request.POST, request.FILES, instance = dish)
            if form.is_valid():
                form = form.save(commit=False)
                form.restaurant = user
                form.save()
                messages.success(request, 'Dish modified successfully.')
                return redirect('index')
    else:
        messages.error(request, 'You are not authorized to modify others menu.')
        return redirect('index')
    context = {
        'form_type': 'dish_modification',
        'id' : dish_id,
        'form' : form,

    }
    return render(request, 'menu/dish.html', context=context)


@login_required
def dish_deletion(request, dish_id):
    dish = Dish.objects.get(id = dish_id)
    user = request.user
    restaurant = user
    if str(restaurant) == str(dish.restaurant):
        if request.method == 'POST':
            dish.delete()
            messages.success(request, 'Dish deleted successfully.')
            return redirect('index')
    else:
        messages.error(request, 'You are not authorized to modify others menu.')
        return redirect('index')

    context = {
        'form_type': 'dish_deletion',
        'id' : dish_id,
        'dish' : dish,
    }
    return render(request, 'menu/dish.html', context=context)



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
