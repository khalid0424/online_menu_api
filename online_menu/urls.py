from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, MealViewSet, RestaurantTableViewSet, BillViewSet, OrderViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'meals', MealViewSet, basename='meal')
router.register(r'tables', RestaurantTableViewSet, basename='table')
router.register(r'bills', BillViewSet, basename='bill')
router.register(r'orders', OrderViewSet, basename='order')

urlpatterns = [
    path('api/', include(router.urls)),
]
