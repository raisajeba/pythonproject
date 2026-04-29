from django.db import models
class FoodItem(models.Model):
    Customer_name = models.CharField(max_length=100)
    Phone_number = models.CharField(max_length =100)
    address = models.CharField(max_length = 100)
    food_item = models.CharField(max_length = 100)
    quantity = models.IntegerField(default=0)
    total_price = models.IntegerField(default=0)
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length =100)
    image = models.ImageField
# Create your models here.
