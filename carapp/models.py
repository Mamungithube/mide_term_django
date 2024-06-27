from django.db import models
from brand.models import Brand
from django.contrib.auth.models import User
class car(models.Model):
    car_image = models.ImageField(upload_to="car/media/uploads/")
    car_name = models.CharField(max_length=200)
    car_price = models.IntegerField()
    car_description = models.CharField(max_length=200)
    Brand_name =models.ForeignKey(Brand,on_delete=models.CASCADE)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    car = models.ManyToManyField(car,blank=True)

    def __str__(self):
        return self.user.username
    

class Comment(models.Model):
    car = models.ForeignKey(car, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.name} on {self.car.car_name}"