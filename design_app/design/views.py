from django.shortcuts import render, get_object_or_404
from .models import Photo

# Create your views here.

def gadget(request):
    return render(request, "design/gadget_home.html")

def g_before(request):
    photos = Photo.objects.filter(top="1").order_by("order")#Photoの情報一部を取得
    categories = Photo.objects.filter(top="2")#Photoのsubを取得

    # filtered_photos = [photo for photo in photos if categories.filter(category=photo.category).exists()]
    
    return render(request, "design/gadget_before.html",{"photos":photos, "categories":categories})


def g_after(request):
    photos = Photo.objects.filter(top="1").order_by("order")
    return render(request, "design/gadget_after.html",{"photos":photos})

def g_after_detail(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    photos = Photo.objects.filter(top="1").order_by("order")#Photoの情報一部を取得
    categories = Photo.objects.filter(top="2")#Photoのsubを取得
    return render(request, "design/gadget_detail.html",{'photo': photo, "photos":photos, "categories":categories})




