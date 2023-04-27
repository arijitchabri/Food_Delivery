from django.db import models
from django.contrib.auth.models import User as restaurant
from django.contrib.auth.models import User

# Create your models here.

# Tags are for denoting the food type (e.g main course or starters or dessert)


class Tags(models.Model):
    tag = models.CharField(max_length=100)
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return f'{self.tag}'

# Dish are the dishes offered my various restaurants.


class Dish(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, null = False, blank = False, default = 'newItem')
    description = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(null = False, blank = False)
    tags = models.ForeignKey(Tags, on_delete = models.CASCADE, null = True)
    restaurant = models.ForeignKey(restaurant, on_delete = models.CASCADE)
    
    def __str__(self):
        return f'{self.name} {self.price} {self.tags}'
    
# Designation is for the customers if its a end user or a restaurant


class Designation(models.Model):
    id = models.AutoField(primary_key = True)
    designation = models.CharField(max_length = 20)

    def __str__(self):
        return f'{self.designation}'


def get_default_designation():              # By default the designation is set to user
    return Designation.objects.get(id = 2)


# Customer is in a one to one relationship with the Django user


class Customer(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=400)
    ph = models.BigIntegerField()
    user = models.OneToOneField(User, on_delete = models.CASCADE)   # Django user module
    designation = models.ForeignKey(Designation, on_delete = models.CASCADE,
                                    null=True, default = get_default_designation)   # Can only be change by admin.

    def __str__(self):
        return f'{self.id}    {self.name}'
    


