from django.shortcuts import render, redirect
from time import strftime
from random import randint

def index(request):
  if "total" not in request.session:
    request.session["total"] = 0
  if "actions" not in request.session:
    request.session["actions"] = []
  return render(request, "index.html")

def start(request):
  if request.method == "POST":
    request.session["max_move"] = request.POST["max_move"]
    request.session["target_gold"] = request.POST["target_gold"]
  return redirect("/")

def process_money(request, place):
  rules = {
    "farm": randint(10,20),
    "cave": randint(5,10),
    "house":  randint(2,5),
    "casino": randint(-50,50)
  }
  time = strftime("%Y/%m/%d %H:%M %p")
  gold = rules[place]
  request.session["total"] += gold
  if gold < 0:
    action = "red", f"entered casino and lost {-gold} golds...Ouch... ({time})"
  elif gold > 0:
    action = "green", f"earned {gold} from {place}! ({time})"
  else:
    action = "gray", f"entered casino and you got nothing... ({time})"
  request.session["actions"].append(action)
  return redirect("/")

def reset(request):
  request.session.clear()
  return redirect("/")
