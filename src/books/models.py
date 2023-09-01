"""Books app models."""

from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):
    """Books model."""

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    subtitle = models.CharField(max_length=120)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    isbn = models.CharField(max_length=13)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Book string representation."""
        return f"{self.title}"

    class Meta:
        """Book metadata."""

        ordering = ("-created",)
