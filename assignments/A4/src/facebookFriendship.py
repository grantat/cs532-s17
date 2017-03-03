# import xml.etree.ElementTree as ET
from pygraphml import GraphMLParser
import csv

def parseXML():

    parser = GraphMLParser()
    graph = parser.parse("output/mln.graphml")
    friends = {}
    counter = 0
    print("Total Nodes:",len(graph.nodes()))
    
    for node in graph.nodes():
        name = node["name"]
        # if there is no friend count visible, don't consider a friend
        try:
            friendCount = node["friend_count"]
            friends[name] =  friendCount
            counter += 1
        except:
            print("No friend count for:",name)

    friends["Michael Nelson"] = counter
    return friends


def writeCSV(friends):
    with open('output/facebookFriends.csv', 'w', newline='') as file:
        for f,count in friends.items():
            writer = csv.writer(file, delimiter=',')
            row = [f,count]
            writer.writerow(row)


if __name__ == "__main__":
    friends = parseXML()
    writeCSV(friends)
    print()