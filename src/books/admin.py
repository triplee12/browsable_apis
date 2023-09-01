"""Books app administration site settings."""

from django.contrib import admin
from .models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    """Register Book in administration site."""

    list_display = [
        'title', 'author', 'isbn',
        'created', 'updated'
    ]
    list_filter = ['title', 'author', 'isbn']
    search_fields = [
        'title', 'author', 'isbn'
    ]
    prepopulated_fields = {'slug': ('title',)}
