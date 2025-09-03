from django.urls import path
from django.urls import path, include
from . import views

urlpatterns = [
      # <-- THIS: all auth views
      path('',views.Home, name = 'Home'),
      path("place/new/",views.PlaceCreate.as_view(), name="place_create"),
]

