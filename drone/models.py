from django.db import models

# Create your models here.
class Drone(models.Model):
    name = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    model_version = models.CharField(max_length=50)
    release_date = models.DateField()
    carrying_capacity = models.FloatField()
    flight_time = models.FloatField()
    max_speed = models.FloatField()
    weight = models.FloatField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='images/drones/')

    class Meta:
        db_table = "drone"

    def __str__(self):
        return self.name
