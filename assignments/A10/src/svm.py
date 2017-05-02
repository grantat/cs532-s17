
from sklearn import svm
from sklearn import cross_validation
import numpy as np


def execSVM(cat, data):
    X = []
    Y = []
    for unit in data:
        vec = data[unit]['vector']
        X.append(vec)
        if data[unit]['actual'] != cat:
            Y.append(-1)
        else:
            Y.append(1)

    dataX = np.array(X)
    dataY = np.array(Y)
    svc = svm.SVC(C=10)
    svc.fit(dataX, dataY)
    score = cross_validation.cross_val_score(svc, dataX, dataY, cv=10)
    return score


def createTabular(cats, newsItems):
    with open("../docs/crossVal.tex", 'w') as f:
        f.write("\hline\n")
        for cat in cats:
            data = execSVM(cat, newsItems)
            outStr = cat + " & "
            mean = 0.0
            for score in data:
                outStr += "%.6f & " % (score)
                mean += score
            mean = mean / len(data)
            outStr += "%.6f " % (mean)
            outStr += "\\\\ \n"
            f.write(outStr)


if __name__ == "__main__":
    newsItems = {}
    with open("data/feedData.txt") as f, open("data/classifiedFeeds.txt") as cf:
        allLines = f.readlines()
        cats = cf.readlines()
        for i, line in enumerate(allLines):
            if i == 0:
                # skip header
                continue
            tuples = line.strip().split('\t')
            feedTitle = tuples[0]
            newsItems[feedTitle] = {}
            newsItems[feedTitle]['vector'] = [float(wc) for wc in tuples[1:]]
            newsItems[feedTitle]['actual'] = cats[i - 1].rstrip()

    cats = ['Android', 'iOS', 'Realm News',
                  'React Native', 'Nodejs', 'Xamarin', 'Databases']

    createTabular(cats, newsItems)
