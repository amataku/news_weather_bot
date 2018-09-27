# coding:utf-8
import requests
import json

def get_news():
    payload = {
        'country' : 'jp',
        'apiKey' : '846b52ee5c4c4a1592c3d0a3f92434dd'
    }

    news_json = requests.get('https://newsapi.org/v2/top-headlines', params = payload).json()

    news = ""

    for news_dict in news_json['articles']:
        title = "[" + news_dict["title"] + "]"
        news += title
        news += "\n"
        news += unicode(news_dict["description"])
        news += "\n"
        news += unicode(news_dict["url"])
        news += "\n"
        news += "\n"

    return news
