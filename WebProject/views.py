from django.shortcuts import render
from drone.models import Drone

def index(request):
    drones = Drone.objects.all()[0]
    context = {'drones':drones}
    return render(request,'index.html',context)