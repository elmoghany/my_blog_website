from django.contrib import admin
from .models import Tag, Author, Post

# Register your models here.
admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Author)