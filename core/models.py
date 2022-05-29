from django.db import models

# Create your models here.
class Category(models.Model):
    CHOICES = (('business','Business'),('culture', 'Culture'),('sport','Sport'),('food','Food'),('politics','Politics'),('celebrity','Celebrity'),('startups','Startups'),('travel','Travel'))
    
    title = models.CharField(max_length=50, choices= CHOICES)    
    created_at = models.DateField(auto_now_add = True)
    description = models.TextField()
    
    def __str__(self):
        return f'{self.title}'

class Slider(models.Model):
    STATUS =  (('active','Active'),('','Inactive'))
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    image = models.ImageField(upload_to = 'media/',blank = True)
    rank = models.IntegerField()

class Comment(models.Model):
    user = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()

        
