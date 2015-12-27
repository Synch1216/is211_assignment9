from bs4 import BeautifulSoup
import requests

myurl = "http://finance.yahoo.com/q/cp?s=^DJI"

html = requests.get(myurl).content
soup = BeautifulSoup(html)

soup.find('span', attrs={'class':'time_rtq_ticker'}).text
u'17,554.47'


