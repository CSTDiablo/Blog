import uuid
from django.db import models

# Create your models here.
class BaseModel(models.Model):
    uuid = models.UUIDField( editable=False , primary_key=True, default=uuid.uuid4)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)
    class Meta:
        abstract = True
    

class Category(BaseModel):
    CHOICES = (('business','Business'),('culture', 'Culture'),('sport','Sport'),('food','Food'),('politics','Politics'),('celebrity','Celebrity'),('startups','Startups'),('travel','Travel'))
    
    title = models.CharField(max_length=50, choices= CHOICES)    
    description = models.TextField()
 
    class Meta:
        verbose_name_plural = 'Category'

    def __str__(self):
        return f'{self.title}'

class Slider(BaseModel):
    STATUS =  (('active','Active'),('','Inactive'))
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    image = models.ImageField(upload_to = 'media/',blank = True)
    rank = models.IntegerField()

    def __str__(self):
        return f'{self.created_at}&{self.updated_at}'
    class Meta:
        verbose_name_plural = 'Slider'

class Blog(BaseModel):
    category = models.ForeignKey(Category, on_delete= models.CASCADE)
    datetime = models.DateField(auto_now_add= True)
    title = models.CharField(max_length= 100)
    description = models.TextField()
    image = models.ImageField(upload_to = 'media/',blank = True)
    is_trending = models.BooleanField(default= False)
    def __str__(self):
        return f'{self.title}'



class Comment(BaseModel):
    user = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    class Meta:
        verbose_name_plural = 'Comment'

class ContactUs(BaseModel):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=50)
    message = models.TextField(max_length=1000)
    class Meta:
        verbose_name_plural = 'ContactUs'

class Trending(BaseModel):
    category = models.ForeignKey(Category, on_delete= models.CASCADE)
    datetime = models.DateField(auto_now_add= True)
    title = models.CharField(max_length= 100)
    class Meta:
        verbose_name_plural = 'Trending'



        