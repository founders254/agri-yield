from django.urls import path
from .views import get_location_weather_soil

urlpatterns = [
    path("get_data/", get_location_weather_soil, name="get_data"),
]