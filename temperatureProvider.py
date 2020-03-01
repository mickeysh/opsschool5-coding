import json
import sys
from requests import get

access_key = "c0881b3c46a0a56b1812c95f9dfcafbd"
if len(sys.argv) == 1:
    print("You didn't enter a city name")
    exit(-1)
cities = sys.argv[1]
cities = cities.replace(",", ";")
citylist = cities.split(";")
units = "m"
degrees = "celsius"
if len(sys.argv) > 2:
    degrees = sys.argv[2]
    if degrees == "-f":
        units = "f"
        degrees = "fahrenheit"
    elif degrees == "-c":
        degrees = "celsius"
    else:
        print("Invalid degrees term :(")
        exit(-1)

params = {
    'access_key': access_key,
    'units': units
}

for city in citylist:
    city = city.capitalize()
    params["query"] = city
    weatherData = get("http://api.weatherstack.com/current", params)
    weatherJson = json.loads(weatherData.text)
    if ('success' in weatherJson) and (weatherJson["success"] is False):
        print("The city doesn't exist. You should try other cities such as: Dublin, New-York, Ashdod :)")
    else:
        temperature = weatherJson["current"]["temperature"]
        print("The weather in " + city + " today " + str(temperature) + " " + degrees + ".")

