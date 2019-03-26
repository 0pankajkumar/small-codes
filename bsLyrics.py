# -*- coding: utf-8 -*-
# import libraries
import urllib2
from bs4 import BeautifulSoup



# specify the url
quote_page = 'https://www.azlyrics.com/lyrics/linkinpark/intheend.html'

# query the website and return the html to the variable 'page’
page = urllib2.urlopen(quote_page)


# parse the html using beautiful soup and store in variable `soup`
soup = BeautifulSoup(page, 'lxml')
soup = soup.prettify()
cont = str(soup)
for i in cont: 
    if cont == '<!-- Usage of azlyrics.com content by any third-party lyrics provider is prohibited by our licensing agreement. Sorry about that. -->':
	    while cont != '<!-- MxM banner -->':
		    lyric = cont[i]
			
# This lyrics sorting is not working. 
# I want just the Lyrics part of In the end
# <div> is not defined at azlyrics



target = open("InTheEndLyrics.txt",'w')
target.write(str(soup))
