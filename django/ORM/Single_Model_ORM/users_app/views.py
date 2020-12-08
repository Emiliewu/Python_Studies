from django.shortcuts import render, redirect
from .models import Users

def index(request):
  context = {
    "user_info":Users.objects.all()
  }
  return render(request, "index.html", context)

def add(request):
  if request.method == "POST":
    first_name = request.POST["first_name"]
    last_name = request.POST["last_name"]
    email_address = request.POST["email_address"]
    age = request.POST["age"]
    Users.objects.create(first_name = first_name, last_name = last_name, email_address = email_address, age = age)
  return redirect("/")
