from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'core/frontpage.html')

def about(request):
    return render(request, 'core/about.html')