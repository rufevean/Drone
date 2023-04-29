from django.db import models

# Create your models here.
class Drone(models.Model):
    name = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    release_date = models.DateField()
    weight = models.FloatField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='images/drones/')

    #sub fields
    ascent_speed = models.FloatField(blank=True, null=True)
    descent_speed = models.FloatField(blank=True, null=True)
    horizontal_speed = models.FloatField(blank=True, null=True)
    takeoff_altitude = models.IntegerField(blank=True, null=True)
    max_flight_distance = models.FloatField(blank=True, null=True)
    operating_temperature = models.CharField(max_length=50,blank=True, null=True)
    gps_system = models.CharField(max_length=50,blank=True, null=True)
    internal_storage = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = "drone"

    def __str__(self):
        return self.name

class Battery(models.Model):
    drone = models.ForeignKey(Drone,related_name="battery", on_delete=models.CASCADE)
    capacity = models.IntegerField()
    weight = models.FloatField(blank=True, null=True)
    battery_type = models.CharField(max_length=50,blank=True, null=True)
    charging_temperature = models.CharField(max_length=50,blank=True, null=True)
    charging_time = models.IntegerField()
    class Meta:
        db_table = "battery"

class RemoteController(models.Model):
    drone = models.ForeignKey(Drone, related_name="controller", on_delete=models.CASCADE)
    max_operating_time = models.CharField(max_length=50, blank=True, null=True)
    max_supported_mobile_device_size = models.CharField(max_length=50, blank=True)
    transmitter_power = models.TextField(blank=True, null=True)

    class Meta:
        db_table = "remotecontroller"
class Camera(models.Model):
    drone = models.ForeignKey(Drone, related_name="camera", on_delete=models.CASCADE)
    image_sensor = models.TextField(blank=True, null=True)
    lens = models.TextField(blank=True, null=True)
    iso_range = models.TextField(blank=True, null=True)
    shutter_speed = models.CharField(max_length=50, blank=True, null=True)
    max_image_size = models.CharField(max_length=50, blank=True, null=True)
    photography_modes = models.TextField(blank=True, null=True)
    photo_format = models.CharField(max_length=50, blank=True, null=True)
    video_resolution = models.TextField(blank=True, null=True)
    video_format = models.CharField(max_length=50, blank=True, null=True)
    max_video_bitrate = models.CharField(max_length=50, blank=True, null=True)
    digital_zoom = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        db_table = "camera"
class Sensor(models.Model):
    drone = models.ForeignKey(Drone, related_name="sensor", on_delete=models.CASCADE)
    sensors_type = models.CharField(max_length=100, blank=True, null=True)
    forward = models.TextField(blank=True, null=True)
    backward = models.TextField(blank=True, null=True)
    lateral = models.TextField(blank=True, null=True)
    upward = models.TextField(blank=True, null=True)
    downward = models.TextField(blank=True, null=True)
    class Meta:
        db_table = "sensor"

class VideoTransmission(models.Model):
    drone = models.ForeignKey(Drone, related_name="transmission", on_delete=models.CASCADE)
    live_view_quality = models.CharField(max_length=50, blank=True, null=True)
    operating_frequency = models.TextField(blank=True, null=True)
    transmission_distance_free_interference = models.TextField(blank=True, null=True)
    transmission_distance_interference = models.TextField(blank=True, null=True)
    max_download_speed = models.CharField(max_length=50, blank=True, null=True)
    lowest_latency = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        db_table = "videotransmission"