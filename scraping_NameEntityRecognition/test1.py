import requests
import pandas as pd #for opening .xls file
from bs4 import BeautifulSoup

#headers for imitiating like we are actual browsers asking for info
headers = {
'Host': 'www.mca.gov.in',
'Connection': 'keep-alive',
'Content-Length': '33',
'Cache-Control': 'max-age=0',
'Origin': 'http://www.mca.gov.in',
'Upgrade-Insecure-Requests': '1',
'Content-Type': 'application/x-www-form-urlencoded',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
'Referer': 'http://www.mca.gov.in/mcafoportal/showVerifyDIN.do',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
'Cookie': 'HttpOnly'
}

#getting all DIN values from xls file
xls = pd.ExcelFile("DIN_Values_Test1.xls")
sheetX = xls.parse(0) #0 is the sheet number
DINs = sheetX['DIN']

#for storing all those names
names = []

for i in DINs:
    payload = {'DIN': i}
    r = requests.post("http://www.mca.gov.in/mcafoportal/verifyDIN.do",headers=headers, data=payload)
    #print(r.text)
    soup = BeautifulSoup(r.text, 'html.parser')

    '''
    table = soup.find('table', id='resultsTab1')
    rows = table.findAll('tr')
    #print(rows)
    '''

    value = soup.find('input', {'id': 'directorFullName'}).get('value')
    names.append(value)
    
#Opening csv file for writing the results
fileName = "DINs_with_names.csv"
f = open(fileName, "w")

j = 0

#Writing all the data
for i in DINs:
    f.write(str(i) + "," + names[j] + "\n")
    j += 1
    
    
f.close()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    