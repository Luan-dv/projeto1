from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=65)
    
    def __str__(self):
        return self.name
    

class Recipe(models.Model):
    title =  models.CharField(max_length=65)
    description = models.CharField(max_length=165)
    slug = models.SlugField()
    preparation_time = models.IntegerField()
    preparation_time_unit = models.CharField(max_length=65)
    servings = models.IntegerField()
    servings_unit = models.CharField(max_length=65)
    preparation_step = models.TextField()
    preparation_step_is_html = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True) #no momento da criação, ele gera uma data e não mexe depois!
    uptade_at = models.DateTimeField(auto_now=True) #somente esse campo atualiza
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(upload_to='recipes/covers/%Y/%m/%d', blank=True, default='')

    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, default=None)

    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title