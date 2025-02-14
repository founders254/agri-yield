import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

OPENWEATHER_API_KEY = "90417e69da7c2ace6e778b6adca27717"

@csrf_exempt
def get_weather_data(request):
    try:
        # Get user's IP location
        ip_api_url = "https://ipinfo.io/json"
        location_data = requests.get(ip_api_url).json()
        lat, lon = location_data["loc"].split(",")

        # Fetch weather data
        weather_api_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={OPENWEATHER_API_KEY}&units=metric"
        weather_response = requests.get(weather_api_url).json()

        # Extract relevant data
        temperature = weather_response["main"]["temp"]
        humidity = weather_response["main"]["humidity"]
        rainfall = weather_response.get("rain", {}).get("1h", 0)  # 0 if no rain data

        return JsonResponse({
            "location": location_data.get("city", "Unknown"),
            "temperature": temperature,
            "humidity": humidity,
            "rainfall": rainfall,
        })
    
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)
