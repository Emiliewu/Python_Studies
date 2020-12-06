from django.urls import path
from . import views
urlpatterns = [
  path('', views.root_method),
  path('time_display', views.time_method),
]