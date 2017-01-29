#!/usr/bin/env python3

#Import the necessary methods from tweepy library
import mmap
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = "821042028800802816-E7SvwPXZKJRzazLctidudXhD0X0SgDZ"
access_token_secret = "hfEMDTkVBX6Kf7x8FddjBZi7joxKZIYYJztq1QFQcF8cp"
consumer_key = "RigRve4McsZdYXNpz2rwPRZfx"
consumer_secret = "EuFivjFeWCBmG205shXMjTPb0u56wTXJgRDRhqaWPRQU1CxYjW"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print (data)
        return True

    def on_error(self, status):
        print (status)



def saveOutput(origUri,finalUri):
    # final URIs to file
    try:
        with open('output/finalURIs.txt', 'a+b', 0) as file, \
            mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ) as s:
            if s.find(bytes(finalUri, encoding='utf-8')) != -1:
                print("found")
                return
            else:
                file.write(bytes(finalUri, encoding='utf-8'))
    except (IOError,ValueError):
        with open('output/finalURIs.txt', 'w') as file:
            file.write(finalUri+"\n")

    # write original URIs to separate file
    try:
        with open("output/originalURIs.txt", "a") as file:
            file.write(origUri+"\n")
    except (IOError,ValueError):
        with open("output/originalURIs.txt", "w") as file:
            file.write(origUri+"\n")


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    try:
        stream = Stream(auth, l)
        #This line filter Twitter Streams to capture data by the keywords
        stream.filter(track=['jazz music', 'marcus miller', 'victor wooten','bill evans','the seatbelts','james brown','snarky puppy'])
    except KeyboardInterrupt:
        print()
        exit()
    except:
        print("Error occurred")
        exit()

