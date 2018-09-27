# coding:utf-8
import requests
import json
import get_weather
import os

def send_weather():
    weather = get_weather.get_weather()
    payload_post = {
        'text' : weather
    }

    url = "https://hooks.slack.com/services/" + os.environ['NEWS_SLACK']
    requests.post(url, data = json.dumps(payload_post))

send_weather()
