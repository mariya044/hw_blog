from django.shortcuts import render, get_object_or_404
from news.models import Post


def posts(request):
    posts=Post.objects.all().order_by("id")
    return render(request, "posts.html", {"posts":posts})
# Create your views here.

def posts_view(request, post_id):
    post=get_object_or_404(Post, id=post_id)
    return render(request, "posts_view.html", {"post": post})