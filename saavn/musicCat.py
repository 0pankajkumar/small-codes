import requests
from bs4 import BeautifulSoup


# Collect and parse first page
page = requests.get('https://www.jiosaavn.com/catalogue-full/albums-hindi')
soup = BeautifulSoup(page.text, 'html.parser')

movie_name_list = soup.find(class_='catalog-items')

#print(movie_name_list.prettify())

movie_name_list_items = movie_name_list.find_all('a')

# Use .contents to pull out the <a> tag’s children
for movie_name in movie_name_list_items:
    names = movie_name.contents[0]
    print(names)