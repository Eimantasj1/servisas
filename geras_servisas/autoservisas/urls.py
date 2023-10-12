from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("orders/", views.orders, name="orders"),
    path("contact/", views.contact, name="contact"),
    path("brand/", views.brand, name="brand"),
]