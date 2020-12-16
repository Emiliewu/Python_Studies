from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name="index"),
  path('new', views.new, name="new"),
  path('create', views.create, name="create"),
  path('<show_id>/', views.detail, name="detail"),
  path('<show_id>/edit', views.edit, name="edit"),
  path('<show_id>/update', views.update, name="update"),
  path('<show_id>/destroy', views.delete, name="delete"),
]
