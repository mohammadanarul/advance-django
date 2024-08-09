from django.urls import path
from apps.blog.views import post, like, comments, shares

urlpatterns = [
    path("", post.post_list_view),
    path("post-generate/", post.auto_post_generate),
    path('aws-products/', post.aws_ecommerce_product)
]
