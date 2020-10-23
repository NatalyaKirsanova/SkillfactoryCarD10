from django.contrib import admin
from app_Cars.models import Car
# Register your models here.
@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('manufacturer', 'modelCar', 'year_manufacture','transmission','color')
    pass