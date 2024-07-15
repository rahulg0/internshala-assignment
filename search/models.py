from django.db import models

# Create your models here.

class Restaurant(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255, default=None)
    geolocation = models.CharField(max_length=50, default=None)
    menu = models.JSONField(default=None)
    
    def __str__(self):
        return self.name
    

class Dish(models.Model):
    item = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    restaurant = models.ForeignKey(Restaurant, related_name='item', on_delete=models.CASCADE)

    def __str__(self):
        return self.item


class Detail(models.Model):
    restaurant = models.OneToOneField(Restaurant, on_delete=models.CASCADE, related_name='details')
    name = models.CharField(max_length=255)
    offers = models.JSONField(default=None)
    cuisines = models.JSONField(default=None)
    currency = models.CharField(max_length=255, default=None)
    location = models.JSONField(default=None)
    price_range = models.IntegerField(default=None)
    user_rating = models.JSONField(default=None)
    mezzo_provider = models.CharField(max_length=255, default=None, null=True)
    order_deeplink = models.CharField(max_length=255, default=None, null=True)
    has_table_booking = models.IntegerField(default=None)
    is_delivering_now = models.IntegerField(default=None)

    def __str__(self):
        return self.name