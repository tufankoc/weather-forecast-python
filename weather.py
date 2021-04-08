import requests
import json

url = "http://api.openweathermap.org/data/2.5/weather"
api_key = ''


def getWeather(city):
    params = {'q':city,'appid':api_key,'lang':'tr'}
    data = requests.get(url,params=params).json()
    if data:
        city = data['name'].capitalize()
        country = data['sys']['country']
        temp = int(data['main']['temp']-273.15)
        condition = data['weather'][0]['description']
        return (city,country,temp,condition)

def main(city):
    weather = getWeather(city)
    if weather:
        print('{0},{1}  {2}°C {3}'.format(weather[0],weather[1],weather[2],weather[3]))

main(input("City : "))

