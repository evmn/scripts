from urllib.request import urlopen
import re, time, os, sys
from bs4 import BeautifulSoup

# Returns a list of URLs to books listed on the standardebooks.org website.
def ScrapeEbooks():
	ebook_urls = []
	base_url = "https://standardebooks.org/ebooks/?page="
	root_url = "https://standardebooks.org"
	for i in range(1, 21):
		url = base_url + str(i)
		html = urlopen(url)
		bsObj = BeautifulSoup(html, "lxml")
		titleList = bsObj.find('ol').findAll('li')
		for link in titleList:
			ebook_urls.extend([root_url + link.find('img').get('src')])
	return ebook_urls

def printURL(urls):
	for links in urls:
		print(links)

printURL(ScrapeEbooks())
