import urllib.request
import sys


for line in sys.stdin:

	imgurl, keywords = line.split('@')
	urllib.request.urlretrieve(imgurl, imgurl.split('/')[-1])