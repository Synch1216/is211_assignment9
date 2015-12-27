import urllib2
from bs4 import BeautifulSoup
import csv

url = ('http://nflcombineresults.com/nflcombinedata.php?year=2000&pos=&college=')

page = urllib2.urlopen(url).read()

soup = BeautifulSoup(page)
table = soup.find('table')

f = csv.writer(open("football.csv", "w"))
f.writerow(["touchdowns" ])
# variable to check length of rows
x = (len(table.findAll('tr')) - 1)
# set to run through x
for row in table.findAll('tr')[1:x]:
    col = row.findAll('td')
    touchdowns= col[1].getText()


    player = (touchdowns, )
    f.writerow(player)