# -*- coding: utf-8 -*-
# import libraries
import urllib2
from bs4 import BeautifulSoup



# specify the url
quote_page = 'https://www.maxlaumeister.com/social/'

# query the website and return the html to the variable 'page’
page = urllib2.urlopen(quote_page)


# parse the html using beautiful soup and store in variable `soup`
soup = BeautifulSoup(page, 'lxml')

sensex=soup.find(class_='box3d')
print s.sensex.string

'''for i in soup:
    soup_html = str(soup)

#stri = soup.prettify()
target = open("WikiDump.txt",'w')
target.write(soup_html)


# Take out the <div> of name and get its value
#name_box = soup.find('h1', attrs={'class': 'normal'})

#name = name_box.text.strip() 
# strip() is used to remove starting and trailing

#print name'''