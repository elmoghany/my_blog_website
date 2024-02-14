from django.db import models
from django.core.validators import MinLengthValidator
# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    
class Tag(models.Model):
    caption = models.CharField(max_length=100)
    
class Post(models.Model):
    title = models.CharField(max_length=50)
    excerpt = models.CharField(max_length=300)
    content = models.TextField(validators=[MinLengthValidator(10)])
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True, default="", blank=True, null=False, db_index=True)
    image_name = models.CharField(max_length=50)
    author = models.ForeignKey("blog.Author", on_delete=models.SET_NULL, null=True)
    caption = models.ManyToManyField(Tag)
    
