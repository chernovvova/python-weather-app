from django.contrib.auth.models import User
from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=5)
    users_id = models.ManyToManyField(User, related_name='locations')
    lat = models.DecimalField(max_digits=5, decimal_places=2)
    lon = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        unique_together = (('lat', 'lon'),)

    def __str__(self):
        return f"{self.name}: lat: {self.lat}, lon: {self.lon}"