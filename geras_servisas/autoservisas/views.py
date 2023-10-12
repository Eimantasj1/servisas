from django.shortcuts import render
from . import models


def index(request):
    context = {
        "num_orders": models.OrderLine.objects.count(),
        "num_cars": models.Car.objects.count(),
        "make": models.CarModel.objects.all()
    }
    return render(request, 'library/index.html', context)

def orders(request):
    return render(
        request,
        "library/order_list.html",
        {"orders": models.ServiceOrder.objects.all()}
    )

def contact(request):
    return render(request, "library/contact.html")

def brand(request):
    context = {
        "make": models.CarModel.objects.all()
    }
    return render(request,"library/brand.html", context)