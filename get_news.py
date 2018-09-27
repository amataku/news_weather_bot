# coding:utf-8
import requests
import json
import os

def get_news():
    payload = {
        'country' : 'jp',
        'apiKey' : os.environ['NEWS_API_KEY']
    }

    news_json = requests.get('https://newsapi.org/v2/top-headlines', params = payload).json()

    news = ""

    for news_dict in news_json['articles']:
        title = "[" + news_dict["title"] + "]"
        news += title
        news += "\n"
        news += str(news_dict["description"])
        news += "\n"
        news += str(news_dict["url"])
        news += "\n"
        news += "\n"

    return news
