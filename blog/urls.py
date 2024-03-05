from django.urls import path

from . import views

urlpatterns = [
    # path("", views.starting_page, name="starting-page"), #starting page => empty path
    path("", views.StartingPageView.as_view(), name="starting-page"), #starting page => empty path
    # path("posts", views.posts, name="posts-page"),
    path("posts", views.AllPostsView.as_view(), name="posts-page"),
    # path("posts/<slug:slug>", views.post_detail, name="post-detail-page"), #posts/my-first-post
    path("posts/<slug:slug>", views.SinglePostView.as_view(), name="post-detail-page"), #posts/my-first-post
    # path("posts/<slug>"), #posts/my-first-post
]