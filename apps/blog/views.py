from django.shortcuts import render, HttpResponse, redirect
from django.core.cache import cache
from django.views.decorators.cache import cache_page
from faker import Faker
from apps.blog.models import Post

fake = Faker()


@cache_page(60 * 15, key_prefix="post_list")  # 15 minutes
def post_list_view(request):
    posts = Post.objects.only("title", "description", "schedule_datetime")
    context = {
        "posts": posts,
        "posts_count": posts.count(),
    }
    return render(request, "post-list.html", context)


def create_post_view(request):

    return redirect("/")


def auto_post_generate(request):
    for _ in range(1500):
        Post.objects.create(
            title=fake.name(),
            image=fake.image_url(),
            description=fake.text(),
            schedule_datetime=fake.date_time(),
        )
    return HttpResponse("500 post generated")
