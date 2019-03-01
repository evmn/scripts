from urllib.request import urlopen
import re, time, os, sys
from bs4 import BeautifulSoup
import sqlite3

# Returns a list of URLs to books listed on the standardebooks.org website.
def ScrapeEbooks():
	ebook_urls = []
	base_url = "https://standardebooks.org/ebooks/?page="
	root_url = "https://standardebooks.org"
	for i in range(1, 22):
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
		title = bsObj.find('article').find('h1').get_text()
		author = bsObj.find('article').find('p').get_text()
		image = bsObj.find('article').find('img')
		reading_ease = bsObj.find('aside', attrs={"id":"reading-ease"}).find('p').get_text()
		words = getWords(reading_ease)
		readingeasy = getReadingEasy(reading_ease)
		description = bsObj.find('section', attrs={"id":"description"}).get_text().replace("Description\n","")

		db.execute('''insert into standardebooks(title, author, words, ease, description)  values(?,?,?,?,?)''', (title, author, words, readingeasy, description))
		print(title, "-", author, "\t", words, "\t", readingeasy)
		print(description)

def getWords(readingeasy):
	tmpList = re.findall(r'[\d,\.]+', readingeasy)
	words = int(tmpList[0].replace(",", ""))
	return words

def getReadingEasy(readingeasy):
	tmpList = re.findall(r'[\d,\.]+', readingeasy)
	easy = float(tmpList[len(tmpList)-1])
	return easy

def printURL(urls):
	for links in urls:
		print(links)

#printURL(ScrapeEbooks())

conn = sqlite3.connect('standardebooks.org.db')
db = conn.cursor()
db.execute('''create table standardebooks (title text, author text, words int, ease float, description text)''')
getInfos(ScrapeEbooks())
conn.commit()
