from django.shortcuts import render, HttpResponse
from django.core.cache import cache
from faker import Faker
from blog.models import Post

fake = Faker()


def post_list_view(request):
    posts = cache.get("posts")
    print("cache hit")
    if posts is None:
        print("cache miss")
        posts = Post.objects.only("title", "description", "schedule_datetime")
        cache.set("posts", posts, 60)

    context = {
        "posts": posts,
        "posts_count": posts.count(),
    }

    return render(request, "post-list.html", context)


def auto_post_generate(request):
    for _ in range(1500):
        Post.objects.create(
            title=fake.name(),
            image=fake.image_url(),
            description=fake.text(),
            schedule_datetime=fake.date_time(),
        )
    return HttpResponse("500 post generated")
