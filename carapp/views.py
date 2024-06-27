from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from .forms import ChangeuserData
from .forms import RegistrationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Profile,Comment,car
from .forms import CommentForm
from django.contrib.auth.decorators import login_required

class CustomLoginView(LoginView):
    template_name = 'login.html'
    def get_success_url(self):
        return reverse_lazy('home')

class CustomLogoutView(LogoutView):
    template_name = 'logout.html'
    def get_success_url(self):
        return reverse_lazy('home')
    
class RegistrationView(CreateView):
    model = User
    form_class = RegistrationForm
    template_name = 'registration.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        valid = super().form_valid(form)
        Profile.objects.create(user=self.object)
        return valid


class UpdateUserProfileView(LoginRequiredMixin,UpdateView):
    form_class = ChangeuserData
    template_name = 'profile.html'
    success_url = reverse_lazy('profile')

    def get_object(self):
        return self.request.user

    def form_valid(self, form):
        response = super().form_valid(form)
        return response
    

class CarDetailView(DetailView):
    model = car
    pk_url_kwarg = 'car_id'
    template_name = 'comment.html'
    context_object_name = 'car'

    def post(self, request, *args, **kwargs):
        car_object = self.get_object()
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.car = car_object
            new_comment.save()
            return redirect('car_detail', car_id=car_object.id)
        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(car=self.object)
        context['form'] = CommentForm()
        return context