from django.urls import path
from . import views

urlpatterns = [
  path("", views.index, name="index"),
  path("wall", views.index, name="index"),
  path("register", views.register, name="register"),
  path("login", views.login, name="login"),
  path("create_mg", views.create_mg, name="create_mg"),
  path("create_cm/<mg>", views.create_cm, name="create_cm"),
  path("logout", views.logout, name="logout"),
  path("del_mg/<mg>", views.del_mg, name="del_mg"),
  path("del_cm/<cm>", views.del_cm, name="del_cm"),
]