# Assignment 1

Main program is pdfCrawl.py, written in python 2.7.

Libraries used:

- sys
- BeautifulSoup
- urllib2 
- urlparse (part of urllib in python 3.x)
- httplib (used for connection refusal errors)

To install dependencies use the following command:

```shell
$ pip install -r requirements.txt
```

# Assignment Details

Assignment #1
Due: 11:59pm Sept 26

## 1.  Demonstrate that you know how to use "curl" well enough to:

- correctly POST data to a form.  
- Show that the HTML response that is returned is "correct".  That is, the server should take the arguments you POSTed and build a response accordingly.  
- Save the HTML response to a file and then view that file in a browser and take a screen shot.

## 2.  Write a Python program that:
  
  1. takes as a command line argument a web page
  2. extracts all the links from the page
  3. lists all the links that result in PDF files, and prints out
     the bytes for each of the links.  (note: be sure to follow
     all the redirects until the link terminates with a "200 OK".)
  4. show that the program works on 3 different URIs, one of which
     needs to be: 
     http://www.cs.odu.edu/~mln/teaching/cs532-s17/test/pdfs.html

## 3.  Consider the "bow-tie" graph in the Broder et al. paper (fig 9):

http://www9.org/w9cdrom/160/160.html

Now consider the following graph:

```shell
A --> B
B --> C
C --> D
C --> A
C --> G
E --> F
G --> C
G --> H
I --> H
I --> K
L --> D
M --> A
M --> N
N --> D
O --> A
P --> G
```

For the above graph, give the values for:

```shell
IN: 
SCC: 
OUT: 
Tendrils: 
Tubes: 
Disconnected:
```
