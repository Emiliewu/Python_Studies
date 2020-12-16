from django.shortcuts import render, redirect, HttpResponse
from django.urls import reverse
from django.contrib import messages

from .models import Course, Description, Comment

def index(request):
  return render(request, "index.html", {"courses": Course.objects.all()})

def add(request):
  if request.method == "POST":
    errors1 = Course.objects.basic_validator(request.POST)
    errors2 = Description.objects.basic_validator(request.POST)
    if not (errors1 or errors2):
    # if not errors1 and not errors2:
      name = request.POST["name"]
      desc = request.POST["desc"]
      course = Course.objects.create(name=name)
      Description.objects.create(course=course, desc=desc)
      return redirect(reverse("index"))
    if errors1:
      for value in errors1.values():
        messages.error(request, value)
    if errors2:
      for value in errors2.values():
        messages.error(request, value)
  return redirect(reverse("index"))

def detail(request, course_id):
  course_id = course_id
  course = Course.objects.get(id=course_id)
  desc = Description.objects.get(course=course)
  context = {
    "course": course,
    "desc": desc
  }
  return render(request, "detail.html", context)

def delete(request, course_id):
  course_id = course_id
  Course.objects.get(id=course_id).delete()
  return redirect(reverse("index"))

def comment(request, course_id):
  course_id = course_id
  course = Course.objects.get(id=course_id)
  comments = Comment.objects.filter(course=course)
  context = {
    "course": course,
    "comments": comments
  }
  print(Comment.objects.all())
  return render(request, "comment.html", context)

def commentadd(request, course_id):
  if request.method == "POST":
    errors = Comment.objects.basic_validator(request.POST)
    if errors:
      for value in errors.values():
        messages.error(request, value)
      return redirect(reverse("comment", kwargs={"course_id":course_id}))
    course_id = course_id
    course = Course.objects.get(id=course_id)
    comment = request.POST["comment"]
    Comment.objects.create(course=course, comment=comment)
  return redirect(reverse("comment", kwargs={"course_id":course_id}))

