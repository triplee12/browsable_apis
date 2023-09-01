"""Books application views."""

# from django.shortcuts import render
from django.views.generic import ListView
from .models import Book


class BookListView(ListView):
    """Book list view."""

    model = Book
    template_name = 'books/list.html'
