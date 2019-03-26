import bs4
from bs4 import BeautifulSoup as soup
from urllib2 import urlopen as uReq

#Like a web browser
my_url = "https://www.flipkart.com/"
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
#Closing the internet port

fileName = "flipKartScrapedOffers.csv"
f = open(fileName, "w")
headers = "Product,Offer,Details\n"
headers = headers.encode('utf8')
f.write(headers)

page_soup = soup(page_html, "html.parser")
#page_soup = page_soup.encode('ascii', 'ignore').decode('ascii')
containers = page_soup.findAll("div",{"class":"_2kSfQ4"})   #Finding that div element

for container in containers:
    
    product = (container.find("div",{"class":"iUmrbN"})).text
    product = product.encode('utf8')    #This is added because the above makes product as an ascii or non-unicode which is not supported in python & spits error
    
    offer = (container.find("div",{"class":"BXlZdc"})).text
    offer = offer.encode('utf8')
    
    details = (container.find("div",{"class":"_3o3r66"})).text
    details = details.encode('utf8')
    
    f.write(product + "," + offer + "\n" + details.replace(',','|') + "\n")
    
f.close()    
