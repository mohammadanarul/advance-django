from django.contrib import admin
from apps.blog.models import Post
from apps.blog.froms import PostForm


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    form = PostForm
