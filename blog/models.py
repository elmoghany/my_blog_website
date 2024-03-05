from django.db import models
from django.core.validators import MinLengthValidator
# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
        
class Tag(models.Model):
    caption = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.caption}"

class Post(models.Model):
    title = models.CharField(max_length=50)
    excerpt = models.CharField(max_length=300)
    content = models.TextField(validators=[MinLengthValidator(10)])
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True, default="", blank=True, null=False, db_index=True)
    author = models.ForeignKey("blog.Author", on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField(Tag)
    image = models.ImageField(upload_to="posts", null=True)
    # image_name = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.title}, {self.date}"    
