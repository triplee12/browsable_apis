"""Apis application views."""

from rest_framework import generics
from books.models import Book
from .serializers import BookSerializer


class BookAPIView(generics.ListAPIView):
    """Book API view."""

    queryset = Book.objects.all()
    serializer_class = BookSerializer
