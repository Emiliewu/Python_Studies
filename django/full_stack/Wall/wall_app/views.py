from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages

from .models import User, Message, Comment

def index(request):
  if "user_id" not in request.session:
    return render(request, "log_reg.html")
  user_id = request.session["user_id"]
  username = User.objects.get(id=user_id).first_name
  messages = Message.objects.all().order_by("-create_at")
  valid_cm = Comment.objects.filter(create_at__minute__gte=30)
  context = {
    "messages": messages,
    "username": username,
    "valid_cm": valid_cm
  }
  return render(request, "index.html", context)

def register(request):
  if request.method == "POST":
    res = User.objects.reg_validate(request.POST)
    if res["is_valid"]:
      request.session["user_id"] = res["result"]
      return redirect(reverse("index"))
    errors = res["result"].values()
    for error in errors:
      messages.error(request, error)
  return redirect(reverse("index"))
    
def login(request):
  if request.method == "POST":
    res = User.objects.login_validate(request.POST)
    if res["is_valid"]:
      request.session["user_id"] = res["result"]
      return redirect(reverse("index")) 
    messages.error(request, res["result"])
  return redirect(reverse("index"))

def create_mg(request):
  if request.method == "POST":
    message = request.POST["message"]
    Message.objects.create(message=message, user_id=User.objects.get(id=request.session["user_id"]))
  return redirect(reverse("index")) 

def logout(request):
  request.session.clear()
  messages.success(request, "See you next time!")
  return redirect(reverse("index"))

def create_cm(request, mg):
  if request.method == "POST":
    comment = request.POST["comment"]
    message_id = Message.objects.get(id=mg)
    Comment.objects.create(comment=comment, user_id=User.objects.get(id=request.session["user_id"]), message_id=message_id)
  return redirect(reverse("index")) 

def del_mg(request, mg):
  Message.objects.get(id=mg).delete()
  return redirect(reverse("index")) 

def del_cm(request, cm):
  Comment.objects.get(id=cm).delete()
  return redirect(reverse("index")) 

