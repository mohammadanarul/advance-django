from django.db import models
from django.utils.translation import gettext_lazy as _


class Post(models.Model):
    class PostStatus(models.TextChoices):
        DRAFT = "Draft"
        PUBLISHED = "Published"

    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images/")
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    schedule_datetime = models.DateTimeField(null=True, blank=True)
    created_by = models.ForeignKey(
        "auth.User", on_delete=models.SET_NULL, null=True, blank=True, related_name="+"
    )
    updated_by = models.ForeignKey(
        "auth.User", on_delete=models.SET_NULL, null=True, blank=True, related_name="+"
    )
    status = models.CharField(
        max_length=9, choices=PostStatus.choices, default=PostStatus.DRAFT
    )

    class Meta:
        ordering = ["-pk"]
