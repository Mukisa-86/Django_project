from django.contrib import admin
from .models import Food, Product
# Register your models here.



@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price", "created_at", "update_at")
    search_fields = ("name", "description")
    list_filter = ("created_at",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "category", "price", "expiry")
    search_fields = ("name", "category")
