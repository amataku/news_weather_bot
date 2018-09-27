# coding:utf-8
import requests
import json
import get_news
import os

def send_news():
    news = get_news.get_news()
    payload_post = {
        'text' : news
    }

    url = "https://hooks.slack.com/services/" + os.environ['NEWS_SLACK']
    requests.post(url, data = json.dumps(payload_post))

send_news()
