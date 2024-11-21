from rest_framework.viewsets import ModelViewSet
from .models import Category, Meal, RestaurantTable, Bill, Order
from .serializers import (
    CategorySerializer, 
    MealSerializer, 
    RestaurantTableSerializer, 
    BillSerializer, 
    OrderSerializer
)

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class MealViewSet(ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer

class RestaurantTableViewSet(ModelViewSet):
    queryset = RestaurantTable.objects.all()
    serializer_class = RestaurantTableSerializer

class BillViewSet(ModelViewSet):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer

class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
