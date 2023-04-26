from django.shortcuts import render
from . models import * 
from django.http import HttpResponse
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