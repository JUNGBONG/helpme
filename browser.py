import webbrowser

#url = "https://google.com"
#url = "https://samsung.com"


#url ="https://www.google.com/search?&q=ssafy"
q_list = ["bts","아이유","블랙핑크","위너"]
url ="https://www.google.com/search?&q="

#물음표 뒤에 엔터, 앤드한번마다 엔터, 들여쓰기 하면 좋음,q뒤에 검색어(쿼리값),open 에서 url+검색어로 해도 괜춘,for문 이용
for q in q_list:
    webbrowser.open(url+q)
#requests.get(주소)