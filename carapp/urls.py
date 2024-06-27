from django.urls import path
from .views import  CustomLoginView,RegistrationView,UpdateUserProfileView
from . import views
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('register/', RegistrationView.as_view(), name='register'),
    path('profile/', UpdateUserProfileView.as_view(), name='profile'),
    path('cars/<int:car_id>/', views.CarDetailView.as_view(), name='car_detail'),
]