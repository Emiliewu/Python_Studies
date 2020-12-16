from django.shortcuts import render, redirect,HttpResponse
from django.urls import reverse
from django.contrib import messages

from .models import Show

def index(request):
  return render(request, "index.html", {'shows':Show.objects.all()})

def new(request):
  return render(request,"new.html")

def create(request):
  if request.method == "POST":
    errors = Show.objects.basic_validator(request.POST)
    if not errors:
      title = request.POST["title"]
      network = request.POST["network"]
      release_date = request.POST["release_date"]
      description = request.POST["description"]
      new_show = Show.objects.create(title=title,network=network,release_date=release_date,description=description)
      return redirect(reverse("detail", kwargs={"show_id": new_show.id}))
    for key, value in errors.items():
      messages.error(request, value)
  return redirect(reverse("new"))
  

def detail(request,show_id):
  show_id = show_id
  show = Show.objects.get(id=show_id)
  context = {
    "show": show,
    "show_id": show_id
  }
  return render(request, "detail.html", context)

def edit(request,show_id):
  show_id = show_id
  show = Show.objects.get(id=show_id)
  context = {
    "show": show,
    "show_id": show_id
  }
  return render(request, "edit.html", context)

def update(request,show_id):
  if request.method == "POST":
    errors = Show.objects.basic_validator(request.POST)
    if not errors:
      show_id = show_id
      title = request.POST["title"]
      network = request.POST["network"]
      release_date = request.POST["release_date"]
      description = request.POST["description"]
      Show.objects.filter(id=show_id).update(title=title,network=network,release_date=release_date,description=description)
      return redirect(reverse("edit", kwargs={"show_id": show_id}))
    for key, value in errors.items():
      messages.error(request, value)
  return redirect(reverse("edit", kwargs={"show_id": show_id}))


def delete(request,show_id):
  show_id = show_id
  show_delete = Show.objects.get(id=show_id)
  show_delete.delete()
  return redirect(reverse("index"))

