import os
from bs4 import BeautifulSoup
import re
import codecs


def visible(element):
    if element.parent.name in ['style', 'script', '[document]',
                               'head', 'title']:
        return False
    elif re.match('<!--.*-->', str(element)):
        return False
    return True


def saveProcessed(filename, line):

    filename = "output/processed/" + filename + ".txt"
    if not os.path.exists("output/processed"):
        os.makedirs("output/processed")

    # if not found, create
    try:
        with open(filename, 'a') as file:
            file.write(line + "\n")
    except (IOError, ValueError):
        with open(filename, 'w') as file:
            file.write(line + "\n")


def processHtml():
    for filename in os.listdir("output/html"):
        print(filename)
        with codecs.open("output/html/" + filename, "r", encoding='utf-8',
                         errors='surrogateescape') as fdata:

            soup = BeautifulSoup(fdata, 'html.parser')

            texts = soup.findAll(text=True)
            visible_texts = list(filter(visible, texts))
            for item in visible_texts:

                item = (item.strip())
                if len(item) != 0:
                    try:
                        print(item)
                        md5name = filename[:-5]
                        saveProcessed(md5name, item)
                    except UnicodeEncodeError:
                        # skip bad encodings
                        print("skipped bad utf-8 encoding")


if __name__ == "__main__":
    processHtml()
