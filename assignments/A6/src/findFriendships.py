import tweepy
import json
import csv

# Variables that contains the user credentials to access Twitter API
access_token = "821042028800802816-E7SvwPXZKJRzazLctidudXhD0X0SgDZ"
access_token_secret = "hfEMDTkVBX6Kf7x8FddjBZi7joxKZIYYJztq1QFQcF8cp"
consumer_key = "RigRve4McsZdYXNpz2rwPRZfx"
consumer_secret = "EuFivjFeWCBmG205shXMjTPb0u56wTXJgRDRhqaWPRQU1CxYjW"


def findFriendships(api):
    # limit by 200, used pages instead of items since its less likely to get
    # timed out.
    data = []
    with open('data/chosenFollowers.csv','r') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            data.append(row[1])

    # add phonedude_mln to this list as well. Makes 101 users
    data = ["phonedude_mln"]+data
    print(data)
    # try:
    #     friendship = api.show_friendship(source_screen_name='phonedude_mln',target_screen_name='weiglemc')
    # except:
    #     print("Failed to connect friendship for: ",,"and",)



if __name__ == "__main__":
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True,
                     wait_on_rate_limit_notify=True)
    try:
        findFriendships(api)
    except KeyboardInterrupt:
        print()