
import clusters
import sys


def createDendrogram():
    blogs, colnames, data = clusters.readfile('data/blogdata.txt')
    cluster = clusters.hcluster(data)
    clusters.drawdendrogram(cluster, blogs, jpeg='../docs/q2Dendrogram.jpg')
    f = open("data/q2ASCII.txt", 'w')
    sys.stdout = f
    clusters.printclust(cluster, labels=blogs)
    f.close()
    sys.stderr.close()


def kmeans():
    karr = [5, 10, 20]
    blogs, colnames, data = clusters.readfile('data/blogdata.txt')
    for i in karr:

        kclust, itercount = clusters.kcluster(data, k=i)
        print(kclust)
        f = open("data/kclust_%d.txt" % i, 'w')
        f.write("Iteration count: %d \n" % itercount)
        print(len(kclust))
        for cluster in kclust:
            f.write("****************************\n")
            f.write("[")
            for blogid in cluster:
                f.write(blogs[blogid] + ", ")
            f.write("]\n")


def mds():
    blognames, words, data = clusters.readfile('data/blogdata.txt')
    coords, itercount = clusters.scaledown(data)
    clusters.draw2d(coords, labels=blognames, jpeg='../docs/q4Mds.jpg')
    print ('Iteration count: %d' % itercount)


if __name__ == "__main__":
    '''
    Written in python 2.7
    '''
    createDendrogram()
    kmeans()
    mds()
