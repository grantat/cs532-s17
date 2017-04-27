
import feedparser
import os.path
import requests
import html
import csv
import re


def saveFeed():
    uri = "http://feeds.feedburner.com/realmio"
    try:
        filename = "data/feed.xml"
        if not os.path.isfile(filename):
            resp = requests.get(uri, stream=False, allow_redirects=True, headers={
                'User-Agent': 'Mozilla/5.0'})

            with open(filename, 'w') as f:
                f.write(resp.text)

    except:
        print("Could not get feed")
        exit()


def remove_img_tags(data):
    '''
    Helper to remove img tags from description
    '''
    p = re.compile(r'<img.*?/>')
    return p.sub('', data)


def remove_emojis(data):
    '''
    Helper to remove emojis from description
    '''
    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"  # emoticons
                               u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                               u"\U0001F680-\U0001F6FF"  # transport & map symbols
                               u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                               "]+", flags=re.UNICODE)
    d = emoji_pattern.sub(r'', data)
    return d


def select100(items):
    filename = "data/feed100.txt"
    if not os.path.isfile(filename):
        with open(filename, 'w') as f, open("data/classifiedFeeds.txt", 'r') as o:
            cat = {}
            for j, item in enumerate(o):
                cat[j] = item

            for i, entry in enumerate(items.entries):
                if i < 100:
                    print(entry["title"])
                    # remove html encodings like &amp;
                    t = html.unescape(entry["title"])
                    d = html.unescape(entry["description"])
                    d = remove_img_tags(d)
                    d = remove_emojis(d)
                    for key, value in cat.items():
                        if i == key:
                            f.write(t + "|" + d + "|" + item)
                else:
                    break


def recreate100():
    with open("data/feed100.txt", 'r') as f, open("data/classifiedFeeds.txt", 'w') as out:
        reader = csv.reader(f, delimiter='|')
        for i in reader:
            categ = i[1]
            out.write(categ + '\n')


def createTabular():
    with open("data/feed100.txt", 'r') as f, open("../docs/tabular.tex",
                                                  'w') as t:
        reader = csv.reader(f, delimiter="|")
        for i in reader:
            title = i[0].replace('&', '\&')
            newsType = i[1]
            outStr = title + " & " + newsType + " \\\\ \n"
            outStr += "\hline\n"
            t.write(outStr)


if __name__ == "__main__":
    saveFeed()
    items = feedparser.parse(r"data/feed.xml")
    select100(items)
    # createTabular()
    # recreate100()
