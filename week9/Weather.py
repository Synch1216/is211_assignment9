import urllib2
from BeautifulSoup import BeautifulSoup

page = urllib2.urlopen(
    'http://www.wunderground.com/history/airport/KNYC/2015/4/1/MonthlyHistory.html.').read()
soup = BeautifulSoup(page)
soup.prettify()

print soup
