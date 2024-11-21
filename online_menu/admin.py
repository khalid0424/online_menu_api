from django.contrib import admin
from .models import Category, Meal, RestaurantTable, Bill, Order

admin.site.register(Category)
admin.site.register(Meal)
admin.site.register(RestaurantTable)
admin.site.register(Bill)
admin.site.register(Order)
