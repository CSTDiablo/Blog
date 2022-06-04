from django.shortcuts import render
from .models import (Category,Slider,Comment,ContactUs, Blog,)

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
        'blog': blog,
        'trendings': Blog.objects.filter(is_trending = True)
    }

    return render(request, 'core/frontpage.html', context)

def about(request):
    blog = Blog.objects.all()
    context = {
        'blog':blog
    }
    return render(request, 'core/about.html', context )

def category(request,id):
    cat_id=Category.objects.get(uuid=id)
    blogs=Blog.objects.filter(category_id= cat_id)

    return render(request, 'core/category.html',{
       "blogs":blogs
    })