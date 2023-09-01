"""Apis application serializers."""

from rest_framework import serializers
from books.models import Book


class BookSerializer(serializers.ModelSerializer):
    """Book serializers."""

    class Meta:
        """Book serializers metadata."""

        model = Book
        fields = (
            'title', 'subtitle', 'slug', 'description',
            'author', 'created', 'updated'
        )
