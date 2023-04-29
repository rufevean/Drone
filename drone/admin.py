from django.contrib import admin
from .models import Drone,Battery,RemoteController,Camera,VideoTransmission,Sensor
# Register your models here.
admin.site.register(Drone)
admin.site.register(Camera)
admin.site.register(Battery)
admin.site.register(VideoTransmission)
admin.site.register(Sensor)
admin.site.register(RemoteController)
