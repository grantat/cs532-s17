
from numpredict import *


def estimate(vectorValues, fmeasureVector, rgroupVector):
    nn = knnestimate(vectors.values(), fmeasureVector)
    print("====================================" * 2)
    print("K nearest neighbors of F-Measure")
    print("====================================" * 2)
    kvals = [1, 2, 5, 10, 20]
    for k in kvals:
        print('k =', k)
        for j in range(k):
            print('%s\t%.6f' % (list(vectors.keys())[nn[j][1]], nn[j][0]))

        print("------------------------------------" * 2)
    print()

    print("====================================" * 2)
    print("K nearest neighbors of Web Science and Digital Libraries Research Group")
    print("====================================" * 2)
    nn = knnestimate(vectors.values(), rgroupVector)
    for k in kvals:
        print('k =', k)
        for j in range(k):
            print('%s\t%.6f' % (list(vectors.keys())[nn[j][1]], nn[j][0]))

        print("------------------------------------" * 2)


def getData():
    '''
    get blogdata in tuples and add to specified blog arrays, or
    new dictionary with blog as key
    '''
    fmeasure = 'F-Measure'
    wlblog = 'Web Science and Digital Libraries Research Group'
    vectors = {}
    fmeasureVals = []
    webrVals = []
    with open("data/blogdata.txt", 'r') as f:
        allLines = f.readlines()
        for i, line in enumerate(allLines):
            if i == 0:
                # skip header
                continue
            tuples = line.strip().split('\t')
            if tuples[0] == fmeasure:
                for i in range(1, len(tuples)):
                    fmeasureVals.append(float(tuples[i]))
            elif tuples[0] == wlblog:
                for i in range(1, len(tuples)):
                    webrVals.append(float(tuples[i]))
            else:
                vectors[tuples[0]] = []
                for i in range(1, len(tuples)):
                    vectors[tuples[0]].append(float(tuples[i]))

    return vectors, fmeasureVals, webrVals


if __name__ == "__main__":
    vectors, vectorfm, vectorwb = getData()
    estimate(vectors.values(), vectorfm, vectorwb)
