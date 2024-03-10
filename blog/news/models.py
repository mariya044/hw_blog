from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
from django.utils import timezone
from taggit.managers import TaggableManager


class Post(models.Model):
    title=models.CharField(max_length=250)
    text=models.TextField()
    author=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    created_at=models.DateTimeField(default=timezone.now)
    published_at=models.DateTimeField(blank=True,null=True)
    image=models.ImageField(blank=True,upload_to="post_images")
    tags=TaggableManager()

    def __str__(self):
        return self.title
# Create your models here.



class Comments(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return "{}".format(self.user)


