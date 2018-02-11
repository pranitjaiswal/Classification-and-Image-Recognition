import urllib.request
from bs4 import BeautifulSoup
import sys


def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""


for line in sys.stdin.readlines():
	idno,pagelink=line.split(';')
	r = urllib.request.urlopen('http'+pagelink).read()
	soup = BeautifulSoup(r,"html.parser")
	#print(soup.prettify())
	url = soup.find_all("li", class_="utility-menu__item utility-menu__item--download")
	#print(url)
	hreftext=url[0].a['href']
	imglink=find_between(hreftext,"'","'")
	print(imglink)