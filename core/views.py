from django.shortcuts import render
from .models import (Category,Slider,Comment,ContactUs)

# Create your views here.

def home(request):
    c = Category.objects.all()
    s = Slider.objects.all()
    C = Comment.objects.all()
    Co = ContactUs.objects.all()
    context = {
        'category': c,
        'slider': s,
        'comment': C,
        'contactus': Co,
    }
    return render(request, 'core/frontpage.html', context)

def about(request):
    return render(request, 'core/about.html')