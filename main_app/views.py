from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy, reverse
from django.views.generic import FormView
from .models import Place
from django.contrib.auth.models import User # this is the user model we use to log in
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from  .forms import PlaceForm


# class SignUpView(FormView):
#     template_name = "signup.html"
#     form_class = UserCreationForm
#     success_url = reverse_lazy("login")  # or your home

def Home(request):
    return render(request, 'home.html')

class PlaceCreate(CreateView):
    model = Place
    form_class= PlaceForm
    template_name = "place/place_form.html"

    def form_valid(self, form):
        
        form = super().form_valid(form)
        form['creator'] = self.request.creator
        return form
    

    def get_success_url(self):
        return reverse("place_detail", kwargs={"pk": self.object.pk})

class PlaceList(ListView):
    model = Place
    template_name = "place/place_list.html"
    context_object_name = "places"

class PlaceDetail(DetailView):
    model = Place
    template_name = "place/place_detail.html"
    context_object_name = "place"

class PlaceDelete(DeleteView):
    model = Place
    success_url = reverse_lazy("place_list")

class PlaceUpdate(UpdateView):
    model = Place
    form_class = PlaceForm
    template_name = "place/place_form.html"

    def get_success_url(self):
        return reverse("place_detail", kwargs={"pk": self.object.pk})
    

class SignUpView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = 'signup.html'
    
