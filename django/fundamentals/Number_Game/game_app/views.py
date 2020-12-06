from django.shortcuts import render, redirect
from random import randint

def index(request):
  if "number" not in request.session:
    request.session["number"] = randint(1, 100)
    print(request.session["number"])
  if "guess" not in request.session:
    request.session["guess"] = 0
  if "counter" not in request.session:
    request.session["counter"] = 0
  return render(request, "index.html")

def compare(request):
  if request.method == "POST":
    guess = request.POST["guess"]
    request.session["guess"] = int(guess)
    request.session["counter"] += 1
  return redirect("/")

def reset(request):
  # request.session["*"].clear()
  del request.session["guess"]
  del request.session["number"]
  del request.session["counter"]
  return redirect("/")
