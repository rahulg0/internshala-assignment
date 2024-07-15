from django.contrib import admin
from . import models


# Register your models here.
@admin.register(models.Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    ordering = ['name']

@admin.register(models.Dish)
class DishAdmin(admin.ModelAdmin):
    ordering = ['item']

@admin.register(models.Detail)
class DetailsAdmin(admin.ModelAdmin):
    ordering = ['name']


