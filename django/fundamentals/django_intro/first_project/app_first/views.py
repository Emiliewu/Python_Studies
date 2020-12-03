# from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse
def index(request):
    return HttpResponse("this is the equivalent of @app.route('/')!")

# from django.shortcuts import render, HttpResponse
# def index(request):
#     return HttpResponse("response from index method from root route, localhost:8000!")
