
import feedparser
import os.path


def getFeed():
    recent100 = "data/top100.txt"
    if os.path.isfile(recent100):
        print()
    pass


if __name__ == "__main__":
    items = feedparser.parse("http://feeds.feedburner.com/realmio")
    for i, entry in enumerate(items.entries):
        print(entry["title"])
