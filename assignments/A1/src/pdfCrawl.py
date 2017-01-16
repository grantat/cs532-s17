# filename : pdfCrawl.py
# Grant Atkins
# (CS 532), Spring 2017
# Assignment 1 - pdfCrawl.py

import sys
from bs4 import BeautifulSoup
from urllib2 import urlopen, HTTPError, URLError


def findPdfs(html):
	"""
	Take html string as parameter and parse through links ('a' elements).
	"""
	pdfs = []
	soup = BeautifulSoup(html, 'html.parser')
	for link in soup.find_all('a'):
   		linkFound = link.get('href')
   		resp = request(linkFound)
   		print linkFound,resp.getcode()
   		finalURL = resp.geturl()
   		contentType = resp.info().type
   		print "Bytes: ",len(resp.read()),"\n"
   		if 'pdf' in contentType:
   			pdfs.append(finalURL)
   	return pdfs


def request(uri):
	"""
	Params: URI to be requested
	Return: http get response
	"""
	try:
		response = urlopen(uri)
		return response
	except HTTPError as e:
		if '\n' in e.reason:
		    errorReason = e.reason.index('\n')
		    print 'Error: ', e.reason[:errorReason]
		else:
			print 'Error: File not found'
	except URLError as e:
	    print 'We failed to reach a server.'
	    print 'Reason: ', e.reason


def determinteBytes(pdfs):
	"""
	
	"""
	print ""
	for link in pdfs:
		print link


if len(sys.argv) == 2:
	response = request(sys.argv[1])
	pdfs = findPdfs(response.read())
	determinteBytes(pdfs)
else:
	print "Usage: python pdfCrawl.py URI"
	exit()
