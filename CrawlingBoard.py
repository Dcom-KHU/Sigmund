# CrawlingBoard 클래스
# 생성자의 첫 번째 인자로는 가져오고 싶은 수량, 두 번째 인자로는 가져오고 싶은 페이지를 입력한다.
# 가져오고 싶은 수량은 15를 넘길 수 없다.
# 링크 에러 발생할 경우 리스트에 추가 하지 않거나, 빈 문자열을 반환 한다.

from bs4 import BeautifulSoup
import requests
import json
from json import dumps, loads, JSONEncoder, JSONDecoder
import time
import re


class CrawlingBoard :
    def __init__(self, num=15, page=1):
        if num <= 0:
            self.num = 1
        else:
            self.num = num
        
        if page <= 0:
            self.page = 1
        else:
            self.page = page

        self.json = ""

    # 에러 코드
    # 0 : 정상
    # 1 : URL 요청 실패
    def Crawling(self):
        Base_URL = "https://www.wevity.com"
        URL = "https://www.wevity.com/?c=find&s=1&gub=1&cidx=21&gp=" + str(self.page)
        resp = requests.get(URL)
        if resp.status_code != 200:
            return ""
        
        html = resp.text
        soup = BeautifulSoup(html, 'html.parser')

        board_list = soup.select("div.ms-list li")

        board_list.pop(0)

        challenge = []

        for i in board_list:
            link = i.find('div', {"class" : "tit"}).a["href"]
            title = i.find('div', {"class" : "tit"}).a.text.strip()

            temp_link = requests.get(Base_URL + link)

            if temp_link.status_code != 200:
                continue
            temp_soup = BeautifulSoup(temp_link.text, 'html.parser')

            temp_tag = list(map(lambda x : x.text[x.text.find("</span>") + 7:].strip(), temp_soup.select("ul.cd-info-list li")))
            
            field = temp_tag[0]
            target = temp_tag[1]
            organization = temp_tag[2]
            date = temp_tag[4][:23]
            price = temp_tag[5]
            won_price = temp_tag[6]
            homepage = temp_tag[7]
            img = Base_URL + temp_soup.select_one('div.cd-area div.img div.thumb').img['src'].strip()

            challenge.append({"link":Base_URL + link,"title":title,"field":field,"target":target,"organization":organization,"date":date,"price":price,"won_price":won_price,"homepage":homepage,"img":img})          

        return json.dumps(challenge, ensure_ascii=False)