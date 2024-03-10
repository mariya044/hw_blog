from django.contrib import admin
from news.models import Post,Comments


class PostModelAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "created_at"]


admin.site.register(Post, PostModelAdmin)


# Register your models here.
class CommentsModelAdmin(admin.ModelAdmin):
    list_display = ["user", "post", "text"]


admin.site.register(Comments, CommentsModelAdmin)
