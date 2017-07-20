import tweepy
import json

# Variables that contains the user credentials to access Twitter API
access_token = ""
access_token_secret = ""
consumer_key = ""
consumer_secret = ""


def getFollowers(api):
    # limit by 200, used pages instead of items since its less likely to get
    # timed out.
    for p in tweepy.Cursor(api.followers,
                           screen_name="phonedude_mln", count=200).pages():
        # used extend since json would break for each page
        # print(p)
        for user_obj in p:
            print(json.dumps(user_obj._json))


if __name__ == "__main__":
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True,
                     wait_on_rate_limit_notify=True)
    try:
        getFollowers(api)
    except KeyboardInterrupt:
        print()
