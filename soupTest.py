import requests
from bs4 import BeautifulSoup
matchId="odds back selection-0 back-cell"
base_url = 'https://www.betfair.com/exchange/football/competition?id=129'
params = { 'id': str(matchId) }
r = requests.get(base_url, params=params)
html = r.content.decode('utf-8', 'ignore')
soup = BeautifulSoup(html)

s=soup.find_all(matchId)

print type(s)

t=str(s)

print (t)
