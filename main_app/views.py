from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import FormView


class SignUpView(FormView):
    template_name = "signup.html"
    form_class = UserCreationForm
    success_url = reverse_lazy("login")  # or your home

def Home(request):
    return render(request, 'home.html')