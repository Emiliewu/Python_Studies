from django.shortcuts import render, redirect
import time
from datetime import datetime

def root_method(request):
  return redirect("/time_display")
# ---- the assignment given method to retrieve date and time
# def time_method(request):
#   context = {
#     "time": time.strftime("%Y-%m-%d %H:%M %p")
#   }
#   return render(request,'index.html', context)

# ------another method to retrieve date and time
def time_method(request):
  context = {
    "time": '{:%Y-%m-%d %H:%M %p}'.format(datetime.now())
    # "time": datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M %p')
  }
  return render(request,'index.html', context)
