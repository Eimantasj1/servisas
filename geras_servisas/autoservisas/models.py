from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
import uuid
from django.contrib.auth import get_user_model
from datetime import date
from tinymce.models import HTMLField

User = get_user_model()

class CarModel(models.Model):
    make = models.CharField(_("make"), max_length=100, db_index=True)
    model = models.CharField(_("model"), max_length=100, db_index=True)
    year = models.PositiveIntegerField(_("year"), db_index=True)

    class Meta:
        verbose_name = _("car model")
        verbose_name_plural = _("car models")
        ordering = ["make", "model", "year"]

    def __str__(self):
        return f"{self.make}, {self.model}, {self.year}"

    def get_absolute_url(self):
        return reverse("car_detail", kwargs={"pk": self.pk})

ORDER_STATUS = (
    (0, _("pending")),
    (1, _("in progress")),
    (2, _("completed")),
    (3, _("canceled")),
)

class Car(models.Model):
    customer = models.CharField(_("customer"), max_length=100, db_index=True)
    car_model = models.ForeignKey(
        CarModel,
        verbose_name=_("car model"),
        on_delete=models.CASCADE,
        related_name="cars"
    )
    plate = models.CharField(_("plate"), max_length=100)
    vin = models.CharField(_("VIN"), max_length=17)
    color = models.CharField(_("color"), max_length=20)

    class Meta:
        verbose_name = _("car")
        verbose_name_plural = _("cars")

    def __str__(self):
        return f"{self.customer}, {self.car_model}, {self.plate}, {self.vin}, {self.color}"

    def get_absolute_url(self):
        return reverse("Car_detail", kwargs={"pk": self.pk})

class ServiceOrder(models.Model):
    car = models.ForeignKey(
        Car,
        verbose_name="car",
        on_delete=models.CASCADE,
        related_name="orders"
    )
    date = models.DateField(_("date"), auto_now_add=True)

    class Meta:
        verbose_name = _("service or order")
        verbose_name_plural = _("service or orders")

    def __str__(self):
        return f"{self.date}"

    def get_absolute_url(self):
        return reverse("ServiceOrder_detail", kwargs={"pk": self.pk})

class PartService(models.Model):
    name = models.CharField(_("name"), max_length=100)
    price = models.DecimalField(_("price"), max_digits=20, decimal_places=2)

    class Meta:
        verbose_name = _("partservice")
        verbose_name_plural = _("partservices")

    def __str__(self):
        return f"{self.name}, {self.price}"

    def get_absolute_url(self):
        return reverse("partservice_detail", kwargs={"pk": self.pk})

class OrderLine(models.Model):
    order = models.ForeignKey(
        ServiceOrder,
        verbose_name=_("order"),
        on_delete=models.CASCADE,
        related_name="lines"
    )
    part_service = models.ForeignKey(
        PartService,
        verbose_name=_("part or service"),
        on_delete=models.CASCADE,
        related_name="order_lines"
    )
    quantity = models.IntegerField(_("quantity"), default=1)
    status = models.PositiveIntegerField(_("status"), choices=ORDER_STATUS, default=0)

    class Meta:
        verbose_name = _("order line")
        verbose_name_plural = _("order lines")

    def __str__(self):
        return f"{self.order}, {self.part_service}, {self.quantity}, {self.status}"

    def get_absolute_url(self):
        return reverse("orderline_detail", kwargs={"pk": self.pk})
