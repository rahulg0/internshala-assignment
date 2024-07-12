from django.db import models

# Create your models here.

class RestaurantData(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255, default=None)
    items = models.JSONField(default=None)
    geolocation = models.CharField(max_length=50, default=None)
    fullDetails = models.JSONField(default=None)

    def __str__(self):
        return self.name