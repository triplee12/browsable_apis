"""Books application urls."""

from django.urls import path
from . import views

urlpatterns = [
    path("", views.BookListView.as_view(), name='books_list'),
]
