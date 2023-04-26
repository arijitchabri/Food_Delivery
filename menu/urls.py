from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),

    # search urls

    path('rs/<str:rest>', views.restaurant_search, name = 'restaurant_search'),
    path('ts/<str:tag>', views.tag_search, name = 'tag_search'),

    # user modification

    path('uc', views.user_creation, name = 'user_creation'),
    path('cc', views.customer_creation, name = 'customer_creation'),
    path('log_out', views.log_out, name = 'log_out'),
    path('log_in', views.log_in, name = 'log_in'),

    # dish modification

    path('dc', views.dish_creation, name = 'dish_creation'),
    path('dm', views.dish_modification, name = 'dish_modification'),
    path('dd', views.dish_deletion, name = 'dish_deletion'),

]
