
import requests
from bs4 import BeautifulSoup
import os


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


def deleteNoFeedFiles():
    noneLines = []
    f = open("data/feedList.txt", "r+")
    d = f.readlines()
    f.seek(0)
    for i, line in enumerate(d):
        if 'None' in line:
            noneLines.append(i)
        else:
            f.write(line)
    f.truncate()
    f.close()

    print(noneLines)
    f = open("data/blogList.txt", "r+")
    d = f.readlines()
    f.seek(0)
    for i, line in enumerate(d):
        if i in noneLines:
            # delete file
            fileToDelete = line.split(' ')[0]
            print("Deleting:", fileToDelete)
            os.remove("data/blogs/" + fileToDelete)
        else:
            f.write(line)
    f.truncate()
    f.close()


if __name__ == "__main__":

    with open("data/blogList.txt") as f, open("data/feedList.txt", 'w') as out:
        for line in f:
            filename = line.split(' ')[0]
            feed = getFeed(filename)
            print(feed, file=out)

    deleteNoFeedFiles()
