from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('rs/<str:rest>', views.resturant_search, name = 'resturant_search'),
    path('ts/<str:tag>', views.tag_search, name = 'tag_search'),
    path('uc', views.user_creation, name = 'user_creation'),
    path('cc', views.customer_creation, name = 'customer_creation')
]
