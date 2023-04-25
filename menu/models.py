from django.db import models
from django.contrib.auth.models import User as Resturant

# Create your models here.

class Tags(models.Model):
    tag = models.CharField(max_length=100)
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return f'{self.tag}'


class Dish(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, null = False, blank = False, default = 'newItem')
    description = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(null = False, blank = False)
    tags = models.ManyToManyField('Tags')
    resturant = models.ForeignKey(Resturant, on_delete = models.CASCADE)
    
    def __str__(self):
        return f'{self.name} {self.price} {self.tags}'


