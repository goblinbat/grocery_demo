from django.urls import path
from . import views

urlpatterns = [
    path('', views.my_list, name="myList"),
    path('add/', views.add, name="addItem"),
    path('delete/', views.delete, name="deleteItem"),
]
