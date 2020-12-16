from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from datetime import datetime, timedelta

from .models import User, Msg, Comment

def index(request):
  if "user_id" not in request.session:
    return render(request, "log_reg.html")
  user_id = request.session["user_id"]
  username = User.objects.get(id=user_id).first_name
  user_msg = Msg.objects.all().order_by("-create_at")
  valid_time = datetime.now() - timedelta(minutes=30)
  valid_cm = Comment.objects.filter(create_at__gte=valid_time)
  context = {
    "user_msg": user_msg,
    "username": username,
    "valid_cm":valid_cm
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
    errors = Msg.objects.mg_validate(request.POST)
    if errors:
      for error, value in errors.items():
        messages.error(request, value)
        return redirect(reverse("index"))
    msg = request.POST["msg"]
    Msg.objects.create(msg=msg, user=User.objects.get(id=request.session["user_id"]))
  return redirect(reverse("index")) 

def logout(request):
  request.session.clear()
  messages.success(request, "See you next time!")
  return redirect(reverse("index"))

def create_cm(request, msg):
  if request.method == "POST":
    errors = Comment.objects.cm_validate(request.POST)
    if errors:
      for error, value in errors.items():
        messages.error(request, value)
        return redirect(reverse("index"))
    comment = request.POST["comment"]
    msg = Msg.objects.get(id=msg)
    user = User.objects.get(id=request.session["user_id"])
    Comment.objects.create(comment=comment, user=user, msg=msg)
  return redirect(reverse("index")) 

def del_mg(request, msg):
  Msg.objects.get(id=msg).delete()
  return redirect(reverse("index")) 

def del_cm(request, cmt):
  Comment.objects.get(id=cmt).delete()
  return redirect(reverse("index")) 

