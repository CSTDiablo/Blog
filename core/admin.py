from django.contrib import admin
from .models import (Category, Slider, Comment,)


# Register your models here.
admin.site.register(Category)
admin.site.register(Slider)
admin.site.register(Comment)