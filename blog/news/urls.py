from django.urls import path
from news import views

urlpatterns = [
path('', views.posts, name="posts"),
    path('post/<int:post_id>/', views.posts_view, name="posts_view"),

    ]