import csv
import json
from pprint import pprint as pp

def defineNodes():
    nodes = []
    with open("data/chosenFollowers.csv", 'r') as f:
        reader = csv.reader(f, delimiter=',')
        # name,screen_name,picture for each row
        # manual entry for Dr. Nelson
        temp1 = {'name':'Michael L. Nelson','id':'phonedude_mln','image':'https://pbs.twimg.com/profile_images/959295176/mln-ad-100x130.jpg'}
        nodes.append(temp1)
        for row in reader:
            name = row[0]
            screen_name = row[1]
            pic = row[2]
            temp = {'name':name,'id':screen_name,'image':pic}
            nodes.append(temp)

    return nodes


def defineEdges(nodes):
    edges = []
    with open("data/friendships.csv",'r') as f:
        reader = csv.reader(f,delimiter=',')
        for row in reader:
            source = row[0]
            target = row[1]
            following = row[2]
            followedBy = row[3]
            if following in 'True':
                temp = {}
                # for i,n in enumerate(nodes):
                #     if n["id"] == source:
                #         temp = {'source':i}
                #     if n["id"] == target:
                #         temp = {'target':i}
                temp = {'source':source,'target':target}
                edges.append(temp)
            if followedBy in 'True':
                temp = {}
                # for i,n in enumerate(nodes):
                #     if n["id"] == source:
                #         temp = {'source':i}
                #     if n["id"] == target:
                #         temp = {'target':i}
                temp = {'source':target,'target':source}
                edges.append(temp)

    return edges


def allFollowersGraph():
    nodes = []
    temp1 = {'name':'Michael L. Nelson','id':'phonedude_mln','image':'https://pbs.twimg.com/profile_images/959295176/mln-ad-100x130.jpg'}
    nodes.append(temp1)
    edges = []
    with open("data/phonedudeFollowers.json",'r') as f:
        for i, line in enumerate(f):
            jsLine = json.loads(line)
            name = jsLine["name"]
            screen_name = jsLine["screen_name"]
            pic = jsLine["profile_image_url"]
            temp = {'name':name,'id':screen_name,'image':pic}
            nodes.append(temp)
            edgeTemp = {'source':screen_name,'target':'phonedude_mln'}
            edges.append(edgeTemp)

    return nodes,edges


def buildJson(nodes,edges,filename):
    data = {'nodes':nodes,'links':edges}
    with open(filename,'w') as f:
        dataToJson = json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False)
        # print(dataToJson)
        print(dataToJson,file=f)

    
if __name__ == "__main__":

    nodes = defineNodes()
    edges = defineEdges(nodes)
    buildJson(nodes,edges,"data/friendships.json")

    nodes,edges = allFollowersGraph()
    buildJson(nodes,edges,"data/allFollowersGraph.json")
