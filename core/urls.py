from django import views
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='Blog-Home'),
    path('about', views.about, name='Blog-About'),
    path('category/<int:id>/',views.category, name='Blog-Category')
    
]
