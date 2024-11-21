from django.db import models



class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Meal(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image_file = models.TextField(null=True, blank=True)  # optional
    description = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class RestaurantTable(models.Model):
    STATUS_CHOICES = [
        ('free', 'Free'),
        ('full', 'Full'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    table_num = models.CharField(max_length=20)

    def __str__(self):
        return f"Table {self.table_num} ({self.status})"


class Bill(models.Model):
    table = models.ForeignKey(RestaurantTable, on_delete=models.CASCADE)
    customer = models.CharField(max_length=100, null=True, blank=True)
    total_sum = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    created_datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Bill {self.id} for Table {self.table}"


class Order(models.Model):
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE)
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f"Order {self.id}: {self.quantity}x {self.meal.name}"
    


