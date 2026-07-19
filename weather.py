import requests
from datetime import datetime

API_KEY = "27460df8981336b7f137fb5f40f29066"


def get_weather(city):

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url)
    data = response.json()

    if data["cod"] == 200:

        weather = data["weather"][0]["main"]

        # Weather Emoji
        if weather == "Clear":
            emoji = "☀️"
        elif weather == "Clouds":
            emoji = "☁️"
        elif weather == "Rain":
            emoji = "🌧️"
        elif weather == "Thunderstorm":
            emoji = "⛈️"
        elif weather == "Snow":
            emoji = "❄️"
        elif weather == "Drizzle":
            emoji = "🌦️"
        elif weather == "Mist":
            emoji = "🌫️"
        else:
            emoji = "🌍"


        sunrise_time = datetime.fromtimestamp(
            data["sys"]["sunrise"]
        )

        sunset_time = datetime.fromtimestamp(
            data["sys"]["sunset"]
        )


        weather_data = {

            "city": data["name"],

            "country": data["sys"]["country"],

            "temperature": data["main"]["temp"],

            "feels_like": data["main"]["feels_like"],

            "max_temp": data["main"]["temp_max"],

            "min_temp": data["main"]["temp_min"],

            "humidity": data["main"]["humidity"],

            "pressure": data["main"]["pressure"],

            "weather": weather,

            "description": data["weather"][0]["description"].title(),

            "emoji": emoji,

            "wind_speed": data["wind"]["speed"],

            "wind_direction": data["wind"].get("deg", "N/A"),

            "visibility": data["visibility"] / 1000,

            "latitude": data["coord"]["lat"],

            "longitude": data["coord"]["lon"],

            "cloudiness": data["clouds"]["all"],

            "sunrise": sunrise_time.strftime("%I:%M %p"),

            "sunset": sunset_time.strftime("%I:%M %p")

        }


        return weather_data


    else:

        return None