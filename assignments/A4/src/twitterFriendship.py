import tweepy
import csv

# Variables that contains the user credentials to access Twitter API
access_token = ""
access_token_secret = ""
consumer_key = ""
consumer_secret = ""


def getFollowers(api):
    data = {}
    pageJson = list()
    # limit by 200, used pages instead of items since its less likely to get timed out.
    for p in tweepy.Cursor(api.followers, screen_name="phonedude_mln",count=200).pages():
        # used extend since json would break for each page
        pageJson.extend(p)

    for user in pageJson:
        data[user.screen_name] = user.followers_count

    data["phonedude_mln"] = len(pageJson)
    writeCSV(data,"output/twitterFollowers.csv")


def getFollowing(api):
    data = {}
    pageJson = list()
    # limit by 200
    for p in tweepy.Cursor(api.friends, screen_name="phonedude_mln",count=200).pages():
        # used extend since json would break for each page
        pageJson.extend(p)

    for user in pageJson:
        data[user.screen_name] = user.friends_count

    data["phonedude_mln"] = len(pageJson)
    writeCSV(data,"output/twitterFollowing.csv")


def writeCSV(data, filename):
    with open(filename, 'w', newline='') as file:
        for f, count in data.items():
            writer = csv.writer(file, delimiter=',')
            row = [f, count]
            writer.writerow(row)


if __name__ == "__main__":
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True,
                     wait_on_rate_limit_notify=True)
    try:
        getFollowers(api)
        getFollowing(api)
    except KeyboardInterrupt:
        print()
