from django.shortcuts import render
from django.views.generic.edit import CreateView
from .forms import CustomUserCreatinForm

from django.urls import reverse_lazy
# Create your views here.

class SignUpView(CreateView):
    form_class = CustomUserCreatinForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy('login')