
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


def aws_ecommerce_product(request):
    # import requests
    #
    # url = "https://real-time-amazon-data.p.rapidapi.com/search"
    #
    # querystring = {"query": "Phone", "page": "1", "country": "US", "sort_by": "RELEVANCE", "product_condition": "ALL"}
    #
    # headers = {
    #     "x-rapidapi-key": "df32b04e82msh4625cf614bd66dfp1fedabjsn0873ffced8f9",
    #     "x-rapidapi-host": "real-time-amazon-data.p.rapidapi.com"
    # }
    #
    # response = requests.get(url, headers=headers, params=querystring)
    # print(response.json())

    # import requests
    #
    # url = "https://thesportsdb.p.rapidapi.com/eventsseason.php"
    #
    # querystring = {"s": "2014-2015", "id": "4328"}
    #
    # headers = {
    #     "x-rapidapi-key": "df32b04e82msh4625cf614bd66dfp1fedabjsn0873ffced8f9",
    #     "x-rapidapi-host": "thesportsdb.p.rapidapi.com"
    # }
    #
    # response = requests.get(url, headers=headers, params=querystring)
    #
    # print(response.json())

    # import requests
    #
    # url = "https://weatherapi-com.p.rapidapi.com/current.json"
    #
    # querystring = {"q": "53.1,-0.13"}
    #
    # headers = {
    #     "x-rapidapi-key": "df32b04e82msh4625cf614bd66dfp1fedabjsn0873ffced8f9",
    #     "x-rapidapi-host": "weatherapi-com.p.rapidapi.com"
    # }
    #
    # response = requests.get(url, headers=headers, params=querystring)
    #
    # print(response.json())

    import requests

    url = "https://jsonplaceholder.typicode.com/posts/1"

    querystring = {"query": "San Francisco", "locale": "en_US"}

    # headers = {
    #     "x-rapidapi-key": "df32b04e82msh4625cf614bd66dfp1fedabjsn0873ffced8f9",
    #     "x-rapidapi-host": "hotels-com-free.p.rapidapi.com"
    # }

    response = requests.get(url)
    print(response.json())
    return HttpResponse(response.json())
