from django.shortcuts import render
from . models import * 
# Create your views here.

def index(request):
    dish = Dish.objects.all()
    context = {
        'dish' : dish
    }
    return render(request, 'menu/index.html', context = context)