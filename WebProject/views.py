from django.shortcuts import render
from drone.models import Drone
from django.forms.models import model_to_dict
def index(request):
    drone = Drone.objects.all()[0]
    battery = drone.battery.first()
    controller = drone.controller.first()
    camera = drone.camera.first()
    sensor = drone.sensor.first()
    transmission = drone.transmission.first()
    context = {'drone':drone,
               'battery':battery,
               'controller':controller,
               'camera':camera,
               'sensor':sensor,
               'transmission':transmission,
               }

    return render(request,'index.html',context)