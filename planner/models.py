from django.db import models

# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.name

class PicnicSpot(models.Model):
    name = models.CharField(max_length=100)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    description = models.TextField()
    distance = models.FloatField()

    def __str__(self):
        return self.name

class WeatherSubscription(models.Model):
    email = models.EmailField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    time_slot = models.DateTimeField()

    def __str__(self):
        return f"{self.email} - {self.location.name} - {self.time_slot}"
