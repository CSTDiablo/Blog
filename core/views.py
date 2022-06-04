from multiprocessing import context
from django.shortcuts import render, redirect
from .models import (Category,Slider,Comment,ContactUs, Blog,Trending,)
from .forms import (ContactForm,)
from django.contrib import messages

# Create your views here.

def home(request):
    category = Category.objects.all()
    slider = Slider.objects.all()
    comment = Comment.objects.all()
    contactus = ContactUs.objects.all()
    search = request.GET.get('search')
    # try:
    if not search:
        blog = Blog.objects.all()   
    else:
        blog = Blog.objects.filter(name__icontains = search)
    # except:
        # pass 
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
    blogsss=Blog.objects.filter(category_id= categories)

    return render(request, 'core/category.html',{
       "category_blogs":blogsss,
       'categorys': categories,
       'trendings': Blog.objects.filter(is_trending = True)

    })

# def categories(request):
#     trending = Trending.objects.all()
#     context = {
#         'trendings':trending
#     }
#     return render(request, 'core/category.html',context)


def contact(request):
    if request.method == "POST":
        form  = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Contact details updated.')
            return redirect('Blog-Contact')
    else:
        form  = ContactForm()
        context = {
            'forms': form
        }
        return render(request, "core/contactus.html",context)

def singlepost(request,id):

    blog = Blog.objects.get(uuid=id)
    context = {
        'blog': blog
    }
    return render(request, 'core/singlepost.html', context)
    