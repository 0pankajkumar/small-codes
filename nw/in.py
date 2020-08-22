from bs4 import BeautifulSoup
import requests

url = 'https://freesearchigrservice.maharashtra.gov.in/'
# r = requests.get(url)	
# print(r.text)
# soup = BeautifulSoup(r.text, 'lxml')
# print(soup)


s = requests.Session()
r = s.get(url)
r2 = s.post(url)

print(r.text)