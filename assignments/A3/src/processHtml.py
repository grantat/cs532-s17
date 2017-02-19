import os
from bs4 import BeautifulSoup
import re


def visible(element):
    if element.parent.name in ['style', 'script', '[document]', 'head', 'title']:
        return False
    elif re.match('<!--.*-->', str(element)):
        return False
    return True


for filename in os.listdir("output/html"):
    print(filename)
    html = open("output/html/"+filename).read()
    soup = BeautifulSoup(html, 'html.parser')

    texts = soup.findAll(text=True)
    visible_texts = list(filter(visible, texts))
    for item in visible_texts:

        item = (item.strip())
        print(type(item))
        # chunks = (phrase.strip() for line in item for phrase in line.split("  "))
        # # texts = ' '.join(chunk for chunk in chunks if chunk)
        # print(chu)
        # print(texts.encode('utf-8'))
    # # kill all script and style elements
    # for script in soup(["script", "style"]):
    #     script.extract()    # rip it out

    # # get text
    # text = soup.get_text()

    # # break into lines and remove leading and trailing space on each
    # lines = (line.strip() for line in text.splitlines())
    # # break multi-headlines into a line each
    # chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # # drop blank lines
    # texts = '\n'.join(chunk for chunk in chunks if chunk)

    # print(texts.encode('utf-8'))
