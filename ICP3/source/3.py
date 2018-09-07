import requests
from bs4 import BeautifulSoup
import urllib.request
url = "https://en.wikipedia.org/wiki/Deep_learning"
source_code = urllib.request.urlopen(url)
plain_text = source_code
s = BeautifulSoup(plain_text, "html.parser")
print("Title is: ",s.title.string)
results = s.find_all('a')
for link in results:
    print(link.get('href'))