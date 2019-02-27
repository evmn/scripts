# Download books from standardebooks.org

Use this script to get all book pages:

```py
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
			ebook_urls.extend([root_url + link.find('a').get('href')])
	return ebook_urls

def printURL(urls):
	for links in urls:
		print(links)

printURL(ScrapeEbooks())
```

```
cut -d "/" -f 5 books >author
cut -d "/" -f 6 books >title
```

Book name is `author_title.azw3` format.

## Scraping 20+239 web page, and make a textbook


```py
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
			ebook_urls.extend([root_url + link.find('a').get('href')])
	return ebook_urls

def getInfos(links):
	for url in links:
		html = urlopen(url)
		bsObj = BeautifulSoup(html, "lxml")
		title = bsObj.find('article').find('h1')
		author = bsObj.find('article').find('p')
		image = bsObj.find('article').find('img')
		reading_ease = bsObj.find('aside', attrs={"id":"reading-ease"}).find('p')
		description = bsObj.findAll('section', attrs={"id":"description"})
		print(title)
		print("<div align=\"center\">", author.get_text(), "</div>")
		print(image)
		print("<h2>Reading Ease</h2>", reading_ease)
		print(description, "\n")

getInfos(ScrapeEbooks())
```