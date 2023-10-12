from django.contrib import admin
from .models import CarModel, Car, ServiceOrder, PartService, OrderLine


class CarModelAdmin(admin.ModelAdmin):
    list_display = ('make', 'model', 'year')
    search_fields = ('make', 'model', 'year')

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('customer', 'car_model', 'plate', 'vin', 'color')
    search_fields = ('customer', 'car_model__make', 'car_model__model', 'plate', 'vin', 'color')


@admin.register(ServiceOrder)
class ServiceOrderAdmin(admin.ModelAdmin):
    list_display = ('car', 'date')
    search_fields = ('car__customer', 'date')


@admin.register(PartService)
class PartServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    search_fields = ('name',)


@admin.register(OrderLine)
class OrderLineAdmin(admin.ModelAdmin):
    list_display = ('order', 'part_service', 'quantity', 'status')
    list_filter = ('status',)
    search_fields = ('order__car__customer', 'part_service__name', 'quantity', 'status')


admin.site.register(CarModel, CarModelAdmin)
