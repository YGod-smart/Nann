
import requests

class Weather:
    
    def __init__(self):
        pass
    
    def can_handle(self, user_input):
        return user_input.lower().startswith("weather ")
    
    def handle(self, user_input):
        city = user_input[8:]
        return self.get_weather(city)
    
    def get_weather(self, city):

    # ---------- First API: Get coordinates ----------
        geo_url = "https://geocoding-api.open-meteo.com/v1/search"

        geo_params = {
            "name": city,
            "count": 1
        }

        geo_response = requests.get(geo_url, params=geo_params)
        geo_data = geo_response.json()

        results = geo_data.get("results")

        if not results:
            return "I couldn't find that city."

        latitude = results[0]["latitude"]
        longitude = results[0]["longitude"]


    # ---------- Second API: Get weather ----------
        weather_url = "https://api.open-meteo.com/v1/forecast"

        weather_params = {
            "latitude": latitude,
            "longitude": longitude,
            "current": "temperature_2m,wind_speed_10m,weather_code"
        }
        weather_codes = {
            0: "☀️ Clear Sky",
            1: "🌤 Mainly Clear",
            2: "⛅ Partly Cloudy",
            3: "☁️ Overcast",
            45: "🌫 Fog",
            48: "🌫 Depositing Fog",
            51: "🌦 Light Drizzle",
            53: "🌦 Moderate Drizzle",
            55: "🌧 Heavy Drizzle",
            61: "🌦 Light Rain",
            63: "🌧 Rain",
            65: "🌧 Heavy Rain",
            71: "❄️ Light Snow",
            73: "❄️ Snow",
            75: "❄️ Heavy Snow",
            95: "⛈ Thunderstorm"
        }
        
        
        weather_response = requests.get(weather_url, params=weather_params)
        weather_data = weather_response.json()

        current = weather_data["current"]
        code = current["weather_code"]
        description = weather_codes.get(
            code,
            "🌍 Unknown Weather"
        )
        temperature = current["temperature_2m"]
        wind_speed = current["wind_speed_10m"]

        return (
            f"📍 {city.title()}\n"
            f"{description}\n"
            f"🌡 Temperature: {temperature}°C\n"
            f"💨 Wind Speed: {wind_speed} km/h"
        )