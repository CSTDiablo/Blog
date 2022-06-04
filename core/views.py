from django.shortcuts import render
from .models import (Category,Slider,Comment,ContactUs, Blog,Trending,)

# Create your views here.

def home(request):
    category = Category.objects.all()
    slider = Slider.objects.all()
    comment = Comment.objects.all()
    contactus = ContactUs.objects.all()
    blog = Blog.objects.all()
    context = {
        'category': category,
        'slider': slider,
        'comment': comment,
        'contactus': contactus,
        'blogs': blog,
        'trendings': Blog.objects.filter(is_trending = True)
    }

    return render(request, 'core/frontpage.html', context)

def about(request):
    blog = Blog.objects.all()
    context = {
        'about_blog':blog
    }
    return render(request, 'core/about.html', context )

def category(request,id):
    categories=Category.objects.get(uuid=id)
    blogs=Blog.objects.filter(category_id= categories)

    return render(request, 'core/category.html',{
       "category_blogs":blogs,
       'categorys': categories
    })

def categories(request):
    trending = Trending.objects.all()
    context = {
        'trendings':trending
    }
    return render(request, 'core/category.html',context)