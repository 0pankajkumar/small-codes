import requests


s = requests.Session()

r = s.get('https://1337x.to/login')
#r = s.get('https://httpbin.org/cookies')

print(r.text)