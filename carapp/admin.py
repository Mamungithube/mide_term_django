from django.contrib import admin
from carapp.models import car,Profile,Comment
# Register your models here.
admin.site.register(car)
admin.site.register(Profile)
admin.site.register(Comment)