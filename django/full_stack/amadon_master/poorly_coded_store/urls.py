from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("checkout/<int:product_id>", views.checkout, name="checkout"),
    path("order/<int:order_id>", views.order, name="order"),
]
