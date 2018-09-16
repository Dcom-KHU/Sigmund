<<<<<<< HEAD
import requests
import json
import re
from json import dumps, loads, JSONEncoder, JSONDecoder
import time
from datetime import datetime
import datetime

now = datetime.datetime.now()
def strToInt(str):
    result = 0
    result = int(str)
    return result




from bs4 import BeautifulSoup
import requests
def get_html(url):
   _html = ""
   resp = requests.get(url)
   if resp.status_code == 200:
      _html = resp.text
   return _html

URL = "https://www.wevity.com/?c=find&s=1&gub=1&cidx=21"
html = get_html(URL)
soup = BeautifulSoup(html, 'html.parser')


bbs = soup.select("#container > div.content-area > div.content-wrap > div.content")

titles = bbs[0].findAll("div", {"class": "tit"})
url = bbs[0].findAll("a", {"href": "?c=find&s1&gub=1&cidx=21&gbn=view&gp=1&ix=25370"})

challenge = []
for i in range(1, len(titles)):
    
    
    title = ''.join(titles[i].text.split())
    url = ''.join(url[i].text.split())
    j2 = {"title": title ,"URL": url}
    challenge.append(j2)
print(challenge)
print(json.dumps({"challenge":challenge}, indent=2))
=======
import time
from datetime import datetime

d = 20 
s = d* 60*60*24
timestamp = time.mktime(datetime.today().timetuple()) + s
p = datetime.fromtimestamp(timestamp)
print(p)
>>>>>>> 2b362264c0c4889626738bafa8f92f4252b1a640
