from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Book, Author

def index(request):
  return render(request, "index.html", {"books": Book.objects.all()})

def books(request):
  if request.method == "POST":
    title = request.POST["title"]
    desc = request.POST["desc"]
    Book.objects.create(title=title, desc=desc)
  return redirect("/")

def book_detail(request, book_id):
  book = Book.objects.get(id=book_id)
  bookauthors = book.authors.all()
  context = {
    "book": book,
    "book_authors": bookauthors,
    "other_authors": Author.objects.exclude(books=book)
  }
  return render(request, "books.html", context)

def book_author(request, book_id):
  if request.method == "POST":
    author_id = request.POST["author_id"]
    author = Author.objects.get(id=author_id)
    book = Book.objects.get(id=book_id)
    book.authors.add(author)
  return redirect(reverse("books"))

def authors(request):
  return render(request, "authorlist.html", {"authors": Author.objects.all()})

def add_authors(request):
  if request.method == "POST":
    first_name = request.POST["first_name"]
    last_name = request.POST["lastt_name"]
    notes = request.POST["notes"]
    Author.objects.create(first_name=first_name, last_name=last_name, notes=notes)
  return redirect(reverse("authors"))

def author_detail(request, author_id):
  author = Author.objects.get(id=author_id)
  authorbooks = author.books.all()
  context = {
    "author": author,
    "author_books": authorbooks,
    "other_books": Book.objects.exclude(authors=author)
  }
  return render(request, "authors.html", context)

def author_book(request, author_id):
  if request.method == "POST":
    book_id = request.POST["book_id"]
    author = Author.objects.get(id=author_id)
    book = Book.objects.get(id=book_id)
    author.books.add(book)
  return redirect(reverse("authors"))