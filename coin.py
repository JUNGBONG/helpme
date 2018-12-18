import requests
from bs4 import BeautifulSoup
#빗썸 웹크로울링
url ="https://www.bithumb.com/"
res = requests.get(url).text
soup = BeautifulSoup(res,'html.parser')
#coin = soup.select('tbody.coin_list')
coins = soup.select('tbody.coin_list tr')
for coin in coins:
    print(coin.select_one("td:nth-of-type(1) a strong").text)
    print(coin.select_one("td:nth-of-type(2) strong").text)
    print("-----------------------")

