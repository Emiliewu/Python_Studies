from django.urls import path
from . import views

urlpatterns = [
  path("", views.index, name="index"),
  path("courses", views.index, name="index"),
  path("add", views.add, name="add"),
  path("courses/destroy/<course_id>", views.detail, name="detail"),
  path("courses/delete/<course_id>", views.delete, name="delete"),
  path("courses/comment/<course_id>", views.comment, name="comment"),
  path("courses/comment/<course_id>/add", views.commentadd, name="commentadd")
]