from django.shortcuts import redirect, HttpResponse

def index(request):
  return HttpResponse("placeholder to later display a list of all blogs")

def new(request):
  return HttpResponse("placeholder to display a new form to create a new blog")

def create(request):
  return redirect("/blogs")

def show(request, number):
  str = f'placeholder to display blog number: {number}'
  return HttpResponse(str)

def edit(request, number):
  str = f'placeholder to edit blog {number}'
  return HttpResponse(str)

def destroy(request):
  return redirect("/blogs")
