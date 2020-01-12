import click
import json
import sys
from requests import get


@click.command()
@click.option('--token')
@click.option('--city')
@click.option('--T', default='Celsius')
def temperature(token, city, t):
    if token == None:
        print("You didn't enter an access key")
        exit(-1)
    if city == None:
        print("You didn't enter a city name")
        exit(-1)
    city = city.replace(",", ";")
    citylist = city.split(";")
    if t == "Celsius":
        units = "m"
    elif t == "Fahrenheit":
        units = "f"
    else:
        print("Invalid degrees term :(")
        exit(-1)

    params = {
        'access_key': token,
        'units': units
    }

    for onecity in citylist:
        onecity = onecity.capitalize()
        params["query"] = onecity
        weatherData = get("http://api.weatherstack.com/current", params)
        weatherJson = json.loads(weatherData.text)
        if ("success" in weatherJson) and (weatherJson["success"] is False):
            if ("error" in weatherJson) and ("type" in weatherJson["error"]) and (weatherJson["error"]["type"] == "invalid_access_key"):
                print("Invalid token")
                exit(-1)
            else:
                print("The city doesn't exist. You should try other cities such as: Dublin, New-York, Ashdod :)")
        else:
            degrees = weatherJson["current"]["temperature"]
            print("The weather in " + onecity + " today " + str(degrees) + " " + t + ".")


if __name__ == '__main__':
    temperature()