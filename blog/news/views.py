from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DeleteView
from news.models import Post,Comments
from news.forms import PostForm,CommentsForm


def posts(request):
    posts = Post.objects.all().order_by("id")
    return render(request, "posts.html", {"posts": posts})


# Create your views here.

def posts_view(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, "posts_view.html", {"post": post})


def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)  # we dont save   it , unless we will add something
            post.author = request.user
            post.save()
            form.save_m2m()
            return redirect("posts")
        else:
            return redirect("posts")
    else:
        form = PostForm()
    return render(request, "create_post.html", {"form": form})


def edit_post(request,post_id):
    post=get_object_or_404(Post,id=post_id)
    if request.user !=post.author:
        return redirect(f"/posts/{post_id}/")
    if request.method=="GET":
        form=PostForm(instance=post)
    if request.method=='POST':
        form=PostForm(request.POST,instance=post)
        if form.is_valid():
            form.save()
        return redirect("posts")
    return render(request, "edit_post.html", {"form":form,"post": post})

def author(request, author_slug):
    author = User.objects.get(username=author_slug)
    posts = Post.objects.filter(author=author)
    return render(request, "author.html", {"author": author, "posts": posts})


def comments(request, pk):
    post = get_object_or_404(Post, id=pk)
    comments = Comments.objects.filter(post=pk)
    if request.method == "POST":
        form = CommentsForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.post = post
            form.save()
            return redirect("posts")
    else:
        form = CommentsForm()
    return render(request,"comments.html",{"post":post,"comments":comments,"form":form})



class PostDeleteView(DeleteView):
    model=Post
    success_url = "/post/"
    template_name="delete_post.html"
