#!/usr/bin/env python3

#Import the necessary methods from tweepy library
import mmap
import requests
import json
import os
from datetime import datetime
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = "821042028800802816-E7SvwPXZKJRzazLctidudXhD0X0SgDZ"
access_token_secret = "hfEMDTkVBX6Kf7x8FddjBZi7joxKZIYYJztq1QFQcF8cp"
consumer_key = "RigRve4McsZdYXNpz2rwPRZfx"
consumer_secret = "EuFivjFeWCBmG205shXMjTPb0u56wTXJgRDRhqaWPRQU1CxYjW"
# Filter list for bad/inappropriate/repeating domains
blacklist = ['.xyz','.pw','http://artist-rack.com?']


def request(uri):
    try:
        resp = requests.get(uri,stream=True,timeout=5,allow_redirects=True,headers={'User-Agent':'Mozilla/5.0'})
        if resp.status_code == 200:
            print("Original URI:",uri)
            print("Final URI:",resp.url)
            saveOutput(uri,resp.url)
    except KeyboardInterrupt:
        print()
        exit()
    except:
        pass
    

def uriFilter(uri):
    for f in blacklist:
        # for unique youtube URIs just get video id
        if 'youtube.com' in uri and '&' in uri:
            pos = uri.find('&')
            finalURI = uri[:pos]
            return finalURI
        elif f in uri:
            return "THISWILLFAIL"


def saveOutput(origUri,finalUri):
    
    if not os.path.exists("output"):
        os.makedirs("output")
        
    # final URIs to file
    try:
        with open('output/finalURIs.txt', 'a+b', 0) as file, \
            mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ) as s:
            if s.find(bytes(finalUri, encoding='utf-8')) != -1:
                return
            else:
                file.write(bytes(finalUri+"\n", encoding='utf-8'))
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


# This is a basic listener that just prints received tweets to stdout.
# Consider this the main class that calls the functions from before
class StdOutListener(StreamListener):
    
    def on_data(self, data):
        print (data)
        jsonData = json.loads(data)
        uriArr = jsonData['entities']['urls']
        for item in uriArr:
            uri = item['url']
            filteredURI = uriFilter(uri)
            if filteredURI is not None:
                uri = filteredURI
            request(uri)
            
        # handle retweet json
        if 'retweeted_status' in jsonData:
            uriArr = jsonData['retweeted_status']['entities']['urls']
            for item in uriArr:
                uri = item['url']
                filteredURI = uriFilter(uri)
                if filteredURI is not None:
                    uri = filteredURI
                request(uri)
                
        print("finished requests")
        return True

    def on_error(self, status):
        print (status)


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    try:
        stream = Stream(auth, l)
        #This line filter Twitter Streams to capture data by the keywords
        stream.filter(track=['jazz music', 'marcus miller', 'victor wooten','bill evans','the seatbelts','james brown','snarky puppy','jamiroquai','jazz messengers'])
    except KeyboardInterrupt:
        print()
        exit()
    except:
        print("Error occurred - SHUTTING DOWN\n",str(datetime.now()))
        exit()

