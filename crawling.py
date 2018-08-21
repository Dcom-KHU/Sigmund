import requests
import json
from json import dumps, loads, JSONEncoder, JSONDecoder

from bs4 import BeautifulSoup
def get_html(url):
   _html = ""
   resp = requests.get(url)
   if resp.status_code == 200:
      _html = resp.text
   return _html

URL = "https://www.wevity.com/?c=find&s=1&gub=1&cidx=21"
html = get_html(URL)
soup = BeautifulSoup(html, 'html.parser')

#print(soup)



bbs = soup.select("#container > div.content-area > div.content-wrap > div.content")


titles = bbs[0].findAll("div", {"class": "tit"})
organs = bbs[0].findAll("div", {"class": "organ"})
remaindate = bbs[0].findAll("div", {"class": "day"})


for i in range(1, len(titles)):
    j1 = {titles[i].text, organs[i].text, remaindate[i].text}
 

