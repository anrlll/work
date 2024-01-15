from django.shortcuts import render
from .models import Photo

# Create your views here.

def gadget(request):
    return render(request, "design/gadget_home.html")

def g_before(request):
    photos = Photo.objects.filter(top="1").order_by("created_at")
    return render(request, "design/gadget_before.html",{"photos":photos})

def g_after(request):
    photos = Photo.objects.filter(top="1").order_by("created_at")
    return render(request, "design/gadget_after.html",{"photos":photos})




