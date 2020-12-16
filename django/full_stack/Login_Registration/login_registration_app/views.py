from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse

from .models import User

def index(request):
  if "user" in request.session:
    messages.success(request,"Welcome Back!")
    return redirect(reverse("success"))
  return render(request, "index.html")

def register(request):
  if request.method == "POST":
    res = User.objects.reg_validate(request.POST)
    if res["is_valid"]:
      request.session["user"] = res["result"]
      messages.success(request, "Successfully registered!")
      return redirect(reverse("success"))
    errors = res["result"].values()
    for error in errors:
      messages.error(request, error)
  return redirect(reverse("index"))
    
def login(request):
  if request.method == "POST":
    res = User.objects.login_validate(request.POST)
    if res["is_valid"]:
      request.session["user"] = res["result"]
      messages.success(request, "Successfully logged in!")
      return redirect(reverse("success")) 
    messages.error(request, res["result"])
  return redirect(reverse("index"))

def logout(request):
  request.session.clear()
  return redirect(reverse("index"))

def success(request):
  if "user" not in request.session:
    return redirect(reverse("index"))
  user_id = request.session["user"]
  user = User.objects.get(id=user_id)
  return render(request, "success.html", {"user": user})