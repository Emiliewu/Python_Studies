from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('add_dojo/', views.add_dojo, name='add-dojo'),
  path('add_ninja/',views.add_ninja, name='add-ninja'),
  path('delete_dojo/<dojo_id>/', views.delete_dojo, name='delete-dojo'),
]