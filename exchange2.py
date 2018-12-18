import requests
from bs4 import BeautifulSoup
url = "http://info.finance.naver.com/marketindex/exchangeList.nhn"
res = requests.get(url).text
class_list = ["tit","sale"]
soup = BeautifulSoup(res,'html.parser')
picks = soup.select('body > div > table > tbody tr')
for p in picks:

print(picks)
#redireact url을 좀더 짧게 사용 할수 있게 해줌 zzul.li
