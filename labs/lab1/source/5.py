import urllib.request
from bs4 import BeautifulSoup
import os

# Assigning the wiki link to link

Link = "https://www.fantasypros.com/nfl/reports/leaders/qb.php?year=2016"

# Opens the URL
getLink=urllib.request.urlopen(Link)
f = open('gameleaders_in_2016.txt', 'w+')
# Converts to HTML
soup = BeautifulSoup(getLink,  "html.parser")
# Prints Header for the wiki page
print(soup.h1.text)
for link in soup.findAll('div'):
    # Goes to the table and collects data from the class  wiki table sortable plain row headers
   table = soup.find("table", { "class" : "table table-bordered table-striped table-hover" })

# looping all elements in tr tags
for row in table.findAll('tr'):
    for h in row.findAll('th'):
        f.write(h.text+' ')
    for r in row.findAll('td'):
       cells = r.text
        # prints table data  elements
       print(cells)
       f.write(cells+'  ')
    f.write('\n')

       # elements =  finding the rowby th
        # printing  th elements as print(elements.text)
f.close()