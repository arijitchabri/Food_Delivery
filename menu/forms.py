from django import forms
from . models import Customer


class Customer_form(forms.ModelForm):

    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['user', 'designation']
