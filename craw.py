import requests
from bs4 import BeautifulSoup

url = ("https://www.youtube.com/?gl=KR&hl=ko")
res = requests.get(url).text
soup = BeautifulSoup(res,'html.parser')
youtube = soup.select('#endpoint > span.title.style-scope.ytd-guide-entry-renderer')
print(youtube.text)
