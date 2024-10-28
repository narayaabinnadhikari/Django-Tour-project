from django.db import models

# Create your models here.

class Tour(models.Model):
    #origin country, destination, number of days, price of tour.
    origin_country = models.CharField(max_length=99)
    destination_country = models.CharField(max_length=99)
    number_of_nights = models.IntegerField()
    price = models.IntegerField()

