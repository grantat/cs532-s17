import tweepy
import json
import csv
from pprint import pprint as pp

# Variables that contains the user credentials to access Twitter API
access_token = "821042028800802816-E7SvwPXZKJRzazLctidudXhD0X0SgDZ"
access_token_secret = "hfEMDTkVBX6Kf7x8FddjBZi7joxKZIYYJztq1QFQcF8cp"
consumer_key = "RigRve4McsZdYXNpz2rwPRZfx"
consumer_secret = "EuFivjFeWCBmG205shXMjTPb0u56wTXJgRDRhqaWPRQU1CxYjW"


def minimizeConnections():
    '''
    Meant to minimize the the connection calls required to determine
    friendship. Creates a dictionary of 100 users mapped to other users
    who aren't already keys.
    For each Key the formula for number of connections to make:
    for 1 in total:
        Users_to_check = total - iteration_count 
        total += Users_to_check

    New total = 5151, vs 10100 to check
    '''
    data = []
    with open('data/chosenFollowers.csv','r') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            data.append(row[1])

    # add phonedude_mln to this list as well. Makes 101 users
    data = ["phonedude_mln"]+data

    fDict = {}
    for i in data:

        temp = []
        notInDict = True
        for j in data:
            if i != j:
                if j in fDict:
                    # skip user if already in dictionary. Since that user
                    # is already a key inside the dictionary, it means they
                    # already check every other necessary user
                    continue
                else:
                    temp.append(j)
                    fDict[i] = temp
                
    return fDict


def findFriendships(api,data):
    # Will take considerable time
    for i in data:
        for j in data:
            
            if i != j:
                try:
                    print(i,"vs",j)
                    sf = api.show_friendship(source_screen_name=i,target_screen_name=j)
                    fDict["isFollowing"] = sf[0].following
                    fDict["isFollowedBy"] = sf[0].followed_by
                    fDict["source"] = i
                    fDict["target"] = j
                except:
                    print("Failed to connect friendship for: ",i,"and",j)
                    isFollowing = ""
                    isFollowedBy = ""


def writeCSV(data, filename):
    with open(filename, 'a', newline='') as file:
        for d in data.items():
            writer = csv.writer(file, delimiter=',')
            row = [d["name"], d["screen_name"], d["profile_image_url"]]
            writer.writerow(row)


if __name__ == "__main__":
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True,
                     wait_on_rate_limit_notify=True)
    try:
        # findFriendships(api)
        fDict = minimizeConnections()
        # findFriendships(api,fDict)
        pp(fDict)
        # print(fDict)
    except KeyboardInterrupt:
        print()