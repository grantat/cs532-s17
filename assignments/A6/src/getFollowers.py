import tweepy
import json

# Variables that contains the user credentials to access Twitter API
access_token = "821042028800802816-E7SvwPXZKJRzazLctidudXhD0X0SgDZ"
access_token_secret = "hfEMDTkVBX6Kf7x8FddjBZi7joxKZIYYJztq1QFQcF8cp"
consumer_key = "RigRve4McsZdYXNpz2rwPRZfx"
consumer_secret = "EuFivjFeWCBmG205shXMjTPb0u56wTXJgRDRhqaWPRQU1CxYjW"


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
