from django.urls import path
from . import views

urlpatterns = [
  path('', views.index),
  path('destroy_session', views.destroy_session),
  path('increment_by_two', views.increment_by_two),
  path('set_num', views.set_num),
]