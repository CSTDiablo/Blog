from django import views
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='Blog-Home'),
    path('about', views.about, name='Blog-About'),
    path('category/<id>',views.category, name='Blog-Category'),
    # path('categories',views.categories, name= 'Blog-Categories'),
    path("contact", views.contact, name="Blog-Contact"),
    path('singlepost/<id>', views.singlepost, name= 'Blog-SinglePost'),
    
]
