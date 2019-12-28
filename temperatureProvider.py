import json
import sys
from requests import get

cities = sys.argv[1]
citylist = cities.split(",")
degrees = "celsius"
if len(sys.argv) > 2:
    degrees = sys.argv[2]
    if degrees == "-f":
        degrees = "fahrenheit"
    elif degrees == "-c":
        degrees = "celsius"
    else:
        print("Invalid degrees term :(")
        exit(-1)

for city in citylist:
    city = city.capitalize()
    weatherData = get("http://api.weatherstack.com/current?access_key=c0881b3c46a0a56b1812c95f9dfcafbd&query=" + city)
    weatherJson = json.loads(weatherData.text)
    if ('success' in weatherJson) and (weatherJson["success"] is False):
        print("The city doesn't exist. You should try other cities such as: Dublin, New-York, Ashdod :)")
    else:
        temperature = weatherJson["current"]["temperature"]
        if degrees == "fahrenheit":
            temperature = temperature * 9 / 5 + 32

        print("The weather in " + city + " today " + str(temperature) + " " + degrees + ".")

