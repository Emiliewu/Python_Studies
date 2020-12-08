from django.urls import path
from . import views
app_name = "blogs_app"
urlpatterns = [
  path('', views.index),
  path('/new', views.new),
  path('/create', views.create),
  path('/<number>', views.show),
  path('/<number>/edit', views.edit),
  path('/<number>/delete', views.destroy)

]