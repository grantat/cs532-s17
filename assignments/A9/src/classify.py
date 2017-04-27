
import docclass
import feedfilter


def findProb(data, cl):
    for item in data:
        item['Cprob'] = cl.cprob(item['Title'], item["Actual"])
        item['fisherprob'] = cl.fisherprob(item['Title'], item["Actual"])
        print(item)
    return data


def printTabular(data):
    for item in data:
        print()


if __name__ == "__main__":
    cl = docclass.fisherclassifier(docclass.getwords)
    cl.setdb("data/first90-trained.db")
    data = feedfilter.read("data/feed.xml", cl, 90)
    findProb(data, cl)
