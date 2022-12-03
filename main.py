from typing import Union

from fastapi import FastAPI
import requests
from bs4 import BeautifulSoup


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/getTimeStories")
def read_root():
    story_list = []
    URL = "https://time.com"
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, 'html5lib')
    li_tags = soup.find_all("li", {"class": "latest-stories__item"})
    for i in li_tags:
        article_heading = i.h3.text
        article_link = "https://time.com" + i.a.get('href')
        story_list.append({"title": article_heading,"link": article_link})
    
    return story_list
    