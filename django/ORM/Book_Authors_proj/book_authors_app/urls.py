from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name="index"),
  path('books', views.books, name="books"),
  path('books/<book_id>', views.book_detail, name="book_detail"),
  path('authors', views.authors, name="authors"),
  path('add_authors', views.add_authors, name="add_authors"),
  path('authors/<author_id>', views.author_detail, name="author_detail"),
  path('book_author/<book_id>', views.book_author, name="book_author"),
  path('author_book/<author_id>', views.author_book, name="author_book"),
]