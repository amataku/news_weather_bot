# coding:utf-8
import requests
import json
import get_news
import get_weather

def send_news():
    news = get_news.get_news()
    payload_post = {
        'text' : news
    }

    url = "https://hooks.slack.com/services/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"
    requests.post(url, data = json.dumps(payload_post))

def send_weather():
    weather = get_weather.get_weather()
    payload_post = {
        'text' : weather
    }

    url = "https://hooks.slack.com/services/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"
    requests.post(url, data = json.dumps(payload_post))

send_news()
send_weather()
