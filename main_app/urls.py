from django.urls import path
from django.urls import path, include
from . import views

urlpatterns = [
      # <-- THIS: all auth views
      path('',views.Home, name = 'Home'),
      path("places/new/",views.PlaceCreate.as_view(), name="place_create"),
      path("places/", views.PlaceList.as_view(), name="place_list"),
      path("places/<int:pk>/", views.PlaceDetail.as_view(), name="place_detail"),
      path("places/<int:pk>/delete/", views.PlaceDelete.as_view(), name="place_delete"),
      path("places/<int:pk>/edit/", views.PlaceUpdate.as_view(), name="place_update"),
]

