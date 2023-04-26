from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('resturant_search/<str:rest>', views.resturant_search, name = 'resturant_search'),
    path('tag_search/<str:tag>', views.tag_search, name = 'tag_search')
]
