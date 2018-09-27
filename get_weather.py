# coding:utf-8
import requests
import json

def get_weather():
    payload = {
        'city' : '330020'
    }

    weather_json = requests.get('http://weather.livedoor.com/forecast/webservice/json/v1', params = payload).json()

    weather = ""
    weather += weather_json["forecasts"][1]["date"]
    weather += "\n"
    weather += weather_json["forecasts"][1]["telop"]
    weather += "\n"
    weather += u"最高気温 : "
    weather += weather_json["forecasts"][1]["temperature"]["max"]["celsius"]
    weather += u"℃"
    weather += "\n"
    weather += u"最低気温 : "
    weather += weather_json["forecasts"][1]["temperature"]["min"]["celsius"]
    weather += u"℃"

    return weather

get_weather()
