from django.contrib import admin
from blog.models import Post
from blog.froms import PostForm


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    form = PostForm
