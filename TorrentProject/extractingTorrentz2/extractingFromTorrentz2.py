import requests
#import pandas as pd #for opening .xls file
from bs4 import BeautifulSoup

headers = {
	'Host': 'torrentz2.eu',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0',
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	'Accept-Language': 'en-US,en;q=0.5',
	'Accept-Encoding': 'identity',
	'DNT': '1',
	'Connection': 'keep-alive',
	'Upgrade-Insecure-Requests': '1'
}

r = requests.get("https://torrentz2.eu/search?f=",headers=headers)
#print(r.text)

soup = BeautifulSoup(r.text, 'html.parser')
value = soup.find_all('dl')#.get('value')
print(value)