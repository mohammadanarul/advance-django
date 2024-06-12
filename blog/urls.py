from django.urls import path
from blog import views

urlpatterns = [
    path("", views.post_list_view),
    path("post-generate/", views.auto_post_generate),
]
