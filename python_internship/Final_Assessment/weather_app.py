from dotenv import load_dotenv
import os
import requests

load_dotenv()
api_key = os.getenv("API_KEY")

city = input("Enter the city name: ")
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

response = requests.get(url)
data = response.json()
# print(data)
try:
    city_name = data["name"]
    temp_celsius = data["main"]["temp"] - 273.15
    min_temp = data["main"]["temp_min"] - 273.15
    max_temp = data["main"]["temp_max"] - 273.15
    wind_speed = data["wind"]["speed"]
    humidity = data["main"]["humidity"]
    visibility = data["visibility"]
    cloud_coverage = data["clouds"]["all"]
    description = data["weather"][0]["description"]

    print(f"Weather in {city_name}:{temp_celsius:.1f}°C ,{description},humidity {humidity}%,minimum temprature is: {min_temp:.1f}°C,maximum temprature is: {max_temp:.1f}°C,speed of wind is {wind_speed} m/s,cloud coverage is {cloud_coverage} %")
except KeyError:
    print("City not found .check the city name ")
