# filename : pdfCrawl.py
# Grant Atkins
# (CS 532), Spring 2017
# Assignment 1 - pdfCrawl.py

from sys import argv
from bs4 import BeautifulSoup
from urllib2 import *

if len(sys.argv) != 1:
	print "Usage: python pdfCrawl.py URI"
	exit()

# Takes web source string as param, retrieved from response
def findPdfs(html):
	soup = BeautifulSoup(html_doc, 'html.parser')
	for link in soup.find_all('a'):
   		print(link.get('href'))

