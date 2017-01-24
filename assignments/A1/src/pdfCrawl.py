#!/usr/bin/env python

import sys
from bs4 import BeautifulSoup
from urllib2 import urlopen, HTTPError, URLError, Request
from urlparse import urljoin, urlparse
from httplib import BadStatusLine


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

        resp = request(linkFound)
        if resp is not None:
            contentType = resp.info().type
            responseCode = resp.getcode()

            if 'application/pdf' in contentType and responseCode == 200:
                finalURL = resp.geturl()
                print "Original URI:",linkFound
                print "Final URI:",finalURL
                # might not contain it
                try:
                    byteSize = resp.headers['content-length']
                except:
                    byteSize = len(resp.read())
                print "Bytes: ", byteSize, "\n"
                pdfs.append(finalURL)
    return pdfs


def request(uri):
    """
    Params: URI to be requested
    Return: http get response
    """
    try:
        reqHeaders = {'User-Agent':'Mozilla 5.10'}
        req = Request(uri,headers=reqHeaders)
        response = urlopen(req)
        return response
    except (HTTPError,ValueError,URLError) as e:
        pass
    except BadStatusLine:
        # print "**Connection closed early For:**","\n",uri,"\n"
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


if __name__ == "__main__":

    if len(sys.argv) == 2:
        response = request(sys.argv[1])

        if response is None:
            print "Initial link can't be bad"
            print "Must contain http:// or https:// and must be reachable"
            exit()

        pdfs = findPdfs(response.read(),response.geturl())
    else:
        print "Usage: python pdfCrawl.py URI"
        exit()
