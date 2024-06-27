from django.shortcuts import render
from carapp.models import car
from brand.models import Brand

def home(request, brand_slug = None):
    car_data = car.objects.all()
    if brand_slug is not None:
        tmp = Brand.objects.get(slug=brand_slug)
        car_data = car.objects.filter(Brand_name = tmp)
    brands = Brand.objects.all()
    return render(request,'index.html',{'data': car_data,'brand': brands})