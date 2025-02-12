from django.shortcuts import render
import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# API Keys
OPENWEATHER_API_KEY = '90417e69da7c2ace6e778b6adca27717'
SOILGRIDS_API_URL = "https://soilgrids.org/"

@csrf_exempt
def get_location_weather_soil(request):
    """
    Fetches user's location, weather data, and soil information.
    """
    try:
        # Get user location using IP API
        ip_api_url = "https://ipinfo.io/json"
        location_response = requests.get(ip_api_url)
        location_response.raise_for_status()  # Raise error if request fails
        location_data = location_response.json()
        
        city = location_data.get("city", "Unknown")
        lat, lon = location_data.get("loc", "").split(",") if "loc" in location_data else (None, None)

        if not lat or not lon:
            return JsonResponse({"error": "Failed to fetch location data"}, status=500)

        # Fetch weather data from OpenWeatherMap API
        weather_api_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={OPENWEATHER_API_KEY}&units=metric"
        weather_response = requests.get(weather_api_url)
        weather_response.raise_for_status()
        weather_data = weather_response.json()

        temperature = weather_data["main"].get("temp", "N/A")
        humidity = weather_data["main"].get("humidity", "N/A")
        rainfall = weather_data.get("rain", {}).get("1h", 0)
        wind_speed = weather_data["wind"].get("speed", "N/A")
        uv_index = weather_data.get("clouds", {}).get("all", 0)

        # Fetch soil data from SoilGrids API
        soil_api_url = f"{SOILGRIDS_API_URL}?lon={lon}&lat={lat}"
        soil_response = requests.get(soil_api_url)
        soil_response.raise_for_status()
        soil_data = soil_response.json()

        # Extract soil properties safely
        properties = soil_data.get("properties", {})
        soil_type = properties.get("soil_type", {}).get("value", "Unknown")
        soil_ph = properties.get("phh2o", {}).get("value", "Unknown")
        soil_moisture = properties.get("moisture", {}).get("value", "Unknown")

        return JsonResponse({
            "location": city,
            "weather": {
                "temperature": temperature,
                "humidity": humidity,
                "rainfall": rainfall,
                "wind_speed": wind_speed,
                "uv_index": uv_index,
            },
            "soil": {
                "type": soil_type,
                "ph": soil_ph,
                "moisture": soil_moisture,
            }
        })

    except requests.RequestException as e:
        return JsonResponse({"error": f"API request failed: {str(e)}"}, status=500)
