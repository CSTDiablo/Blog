from django.contrib import admin
from .models import (Category, Slider, Comment,ContactUs,Blog,Trending,)


# Register your models here.

admin.site.register(Category)
admin.site.register(Slider)
admin.site.register(Comment)
admin.site.register(ContactUs)
admin.site.register(Blog)
admin.site.register(Trending)
