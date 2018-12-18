import requests
from bs4 import BeautifulSoup
#pip설치 파이썬패키지or모듈 pip install requests
#url ="https://google.com"
url ="https://www.daum.net/"
#원하는 정보 탐색 ex)워너원
#request get("주소") ->꺽쇠안에 스트링값이 들아감, 파이썬에 객체 ex) html코드 등등
#requests.get('주소').text
#request get("주소").status_code
#res = requests.get(url)
res = requests.get(url).text
#res = requests.get(url).status_code
#pip install bs4 로 bs4설치 , from bs4 import BeautifulSoup로 bs4사용, 
#웹에서 내가 원하는 정보 검사 -copy -select copy
soup = BeautifulSoup(res,'html.parser')
'''#트리구조,부모자식, 어떤폴더 안에 어떤폴더안에 어떤폴더 그런느낌!
#soup.select('#mArticle > div.cmain_tmp > div.section_media > div.hot_issue.issue_mini > div.hotissue_layer > ol > li.next > div > div:nth-child(1) > span.txt_issue > a')
#p= soup.select('#mArticle > div.cmain_tmp > div.section_media > div.hot_issue.issue_mini > div.hotissue_layer > ol > li.current > div > div:nth-of-type(1) > span.txt_issue > a')
#bs4에서 적용하기 위해 nth-child 를  nth-of-type'''
#li =>모든 li를 가져와라 nth-of-type, #=아이디, 아무것도없는거=클래스,
picks = soup.select('#mArticle > div.cmain_tmp > div.section_media > div.hotissue_builtin.hide > div.realtime_part > ol > li > div > div:nth-of-type(1) > span.txt_issue > a')
for p in picks:
    print(p.text)