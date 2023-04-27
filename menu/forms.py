from django import forms
from . models import Customer, Dish


class Customer_form(forms.ModelForm):

    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['user', 'designation']

class Dish_creation_Form(forms.ModelForm):

    class Meta:
        model = Dish
        fields = '__all__'
        exclude = ['restaurant']
