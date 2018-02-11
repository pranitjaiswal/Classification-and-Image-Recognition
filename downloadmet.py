import urllib.request
from bs4 import BeautifulSoup #library to scrape webpages
import sys

#function to find substring in a string between two given substrings
def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""


for line in sys.stdin.readlines():
	idno,pagelink=line.split(';') #split CSV link data into id and link
	r = urllib.request.urlopen('http'+pagelink).read() #HTTP request to get link code
	soup = BeautifulSoup(r,"html.parser") #variable storing link code
	#print(soup.prettify())
	url = soup.find_all("li", class_="utility-menu__item utility-menu__item--download") #to find particular li item of the image link
	#print(url)
	hreftext=url[0].a['href'] #to find href content of 'Download' link for image
	imglink=find_between(hreftext,"'","'") #cleans image URL
	print(imglink)
