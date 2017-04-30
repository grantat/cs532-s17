
import docclass
import feedfilter
import os


def findProb(data, cl):
    '''
    Use predefined fisher methods for these probabilities
    '''
    for item in data:
        item['Cprob'] = cl.cprob(item['Title'], item["Actual"])
        item['fisherprob'] = cl.fisherprob(item['Title'], item["Actual"])
        print(item)
    return data


def calcMeasurements(cats, data, trainCount):
    '''
    Method to calculate fmeasure, precision, recall
    TP = True Positive
    FP = False Positive
    FN = False Negative
    '''
    catDict = {}
    for cat in cats:
        TP, FP, FN = 0.0, 0.0, 0.0
        for i, item in enumerate(data):
            if item['Actual'] != cat:
                continue
            if not item['Guess']:
                FN += 1.0
            elif(item['Actual'] == item['Guess']):
                TP += 1.0
            elif(item['Actual'] != item['Guess']):
                FP += 1.0
            print(item['Title'], item['Guess'], item['Actual'], "asdasd")

        prec = TP / (TP + FP)
        recall = 0.0
        if (TP + FN) != 0.0:
            recall = TP / (TP + FN)
        f1 = 0.0
        if (prec + recall) != 0.0:
            f1 = 2 * (prec * recall) / (prec + recall)
        print(cat)
        print(prec)
        print(recall)
        print(f1)
        catDict[cat] = {'prec': prec, 'recall': recall, 'f1': f1}

    return catDict


def printTabular(cats):
    outStr = "\hline\n"
    print(cats)
    for key, val in cats.items():
        outStr += key + " & " + str(val['prec']) + " & " + \
            str(val['recall']) + " & " + str(val['f1']) + " \\\\ \n"

    return outStr


def tabularPredictions(data, trainCount):
    outStr = "\hline\n"
    for i, item in enumerate(data):
        if(i == trainCount):
            outStr += "% TEST SET STARTS HERE\n"
        outStr += item["Title"] + " & " + item["Actual"] + \
            " & " + item["Guess"] + " \\\\ \n"

    return outStr


def resultPred(data):
    '''
    Get set of categories and list of predictions
    '''
    cats = set()
    predicted = []
    for i in data:
        cats.add(i["Actual"])
        predicted.append(i["Guess"])
    return cats, predicted


def removeDbs():
    '''
    Clean databases for each run
    '''
    db1 = "data/first90-trained.db"
    db2 = "data/first50-trained.db"
    if(os.path.isfile(db1)):
        os.remove(db1)
    if(os.path.isfile(db2)):
        os.remove(db2)


if __name__ == "__main__":
    removeDbs()
    trainCount = 90
    cl = docclass.fisherclassifier(docclass.getwords)
    cl.setdb("data/first" + str(trainCount) + "-trained.db")
    data = feedfilter.read("data/feed.xml", cl, trainCount)
    data = findProb(data, cl)
    cats, predicted = resultPred(data)
    catDict = calcMeasurements(cats, data, trainCount)
    # print to files. should only be 1 time run
    # with open("../docs/" + str(trainCount) + "measureTabular.tex", 'w') as f:
    #     outStr = printTabular(catDict)
    #     f.write(outStr)
    # with open("../docs/" + str(trainCount) + "trained.tex", 'w') as f:
    #     outStr = tabularPredictions(data, trainCount)
    #     f.write(outStr)
