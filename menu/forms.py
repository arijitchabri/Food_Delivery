from django import forms
from . models import Customer, Dish


class CustomerForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['user', 'designation']


class DishCreationForm(forms.ModelForm):

    class Meta:
        model = Dish
        fields = '__all__'
        exclude = ['restaurant']
