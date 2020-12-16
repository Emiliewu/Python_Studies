from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Order, Product

def index(request):
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "store/index.html", context)

def checkout(request, product_id):
    if request.method == "POST":
        quantity_from_form = int(request.POST["quantity"])
        # price_from_form = float(request.POST["price"])
        product_price = Product.objects.get(id=product_id).price
        total_charge = quantity_from_form * product_price
        new_order = Order.objects.create(quantity_ordered=quantity_from_form, total_price=total_charge)
    return redirect(reverse("order", kwargs={"order_id": new_order.id}))
    # return redirect(f'/order/{order_id}')


def order(request, order_id):
    order = Order.objects.get(id=order_id)
    orders = Order.objects.all()
    total_quantity = 0
    total_price = 0
    for o in orders:
        total_quantity += o.quantity_ordered
        total_price += o.total_price
    context = {
        "order_id": order_id,
        "order": order,
        "total_quantity": total_quantity,
        "total_price": total_price
    }
    return render(request, "store/checkout.html", context)