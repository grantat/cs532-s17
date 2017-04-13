
import requests
from bs4 import BeautifulSoup
import feedparser


def getFeed(filename):
    print("FILENAME:", filename)
    with open("data/blogs/" + filename) as f:
        f.seek(0)
        html = f.read()
        soup = BeautifulSoup(html, 'html.parser')
        feed = soup.find_all(
            'link', attrs={'type': 'application/atom+xml'})

        if(feed):
            return feed[0]['href']
        return None


if __name__ == "__main__":

    with open("data/blogList.txt") as f, open("data/feedList.txt", 'w') as out:
        for line in f:
            filename = line.split(' ')[0]
            feed = getFeed(filename)
            print(feed, file=out)
