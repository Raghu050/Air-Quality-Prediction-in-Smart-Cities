from django.db import models


class AirPollutionData(models.Model):
    district = models.CharField(max_length=100)
    year = models.IntegerField()
    pollution_level = models.IntegerField()

    def __str__(self):
        return f"{self.district} - {self.year}"



class AirQuality(models.Model):
    District = models.CharField(max_length=100)
    CO = models.FloatField()
    NMHC = models.FloatField()
    C6H6 = models.FloatField()
    NO2 = models.FloatField()
    temp = models.FloatField()
    humidity = models.FloatField()