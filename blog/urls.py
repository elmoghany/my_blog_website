from django.urls import path

urlspatterns = [
    path(""), #starting page => empty path
    path("posts"),
    path("posts/<slug:slug>"), #posts/my-first-post
    # path("posts/<slug>"), #posts/my-first-post
]