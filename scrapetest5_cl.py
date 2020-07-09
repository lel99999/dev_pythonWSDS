from urllib.request import urlopen 
from bs4 import BeautifulSoup
#html = urlopen('http://www.pythonscraping.com/pages/page3.html')
html = urlopen('https://washingtondc.craigslist.org/search/sso?query=bike+specialized&sort=date')
bs = BeautifulSoup(html, 'html.parser')

nameList = bs.findAll('li',{'class':'result-row'})
for name in nameList:
    print(name.get_text())

#for sibling in bs.find('result-row',{'id':'result-image gallery'}).tr.next_siblings:
#    print(sibling)
