# filename : pdfCrawl.py
# Grant Atkins
# (CS 532), Spring 2017
# Assignment 1 - pdfCrawl.py

import sys
from bs4 import BeautifulSoup
from urllib2 import urlopen, HTTPError, URLError
from urlparse import urljoin, urlparse


def findPdfs(html,baseurl):
    """
    Take html string as parameter and parse through links ('a' elements). Print final redirect url and bytes
    Params: html string to be used by beautiful soup, baseurl which is passed from commandline
    Return: Array of urls that end with pdf files
    """
    pdfs = []
    soup = BeautifulSoup(html, 'html.parser')
    for link in soup.find_all('a',href=True):

        linkFound = link.get('href')
        if isAbsolute(linkFound) == False:
            linkFound = urljoin(baseurl,linkFound)

        # print "LINK FOUND:",linkFound
        resp = request(linkFound)
        if resp is not None:
            contentType = resp.info().type
            responseCode = resp.getcode()

            if 'pdf' in contentType and responseCode == 200:
                finalURL = resp.geturl()
                print finalURL
                print "Bytes: ", len(resp.read()), "\n"
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
        pass
    except URLError as e:
        pass
    except KeyboardInterrupt:
        print ""
        exit()


def isAbsolute(url):
    """ 
    Taken from stackoverflow post
    """
    try:
        return bool(urlparse(url).netloc)
    except:
        return False


if len(sys.argv) == 2:
    response = request(sys.argv[1])

    if response is None:
        print "Initial link can't be bad"
        exit()

    pdfs = findPdfs(response.read(),response.geturl())
else:
    print "Usage: python pdfCrawl.py URI"
    exit()
