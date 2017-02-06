#!/usr/bin/env python3

import requests
import os
import json


def saveOutput(uri,count):

    if not os.path.exists("output"):
        os.makedirs("output")

    # Save json received/created to output
    try:
        with open('output/timeMaps.json', 'a+b', 0) as file:
            file.write(bytes(uri + ",\n", encoding='utf-8'))
    except (IOError, ValueError):
        with open('output/finalURIs.txt', 'w') as file:
            file.write(uri + "\n")




def countMementos(jsonResp):
    print()

# Remove unwanted from finalURIs
with open("output/finalURIs.txt", "r") as file:
    lines = file.readlines()
    for num, line in enumerate(lines):
        try:
            timeMapURI = "http://memgator.cs.odu.edu/timemap/json/" + line
            print(timeMapURI)
            resp = requests.get(timeMapURI, stream=True, timeout=5, allow_redirects=True, headers={
                                'User-Agent': 'Mozilla/5.0'})

            if resp.status_code == 200:
                # count through json arr
                print(resp.text)
                print()

        except KeyboardInterrupt:
            print()
            exit()
        except:
            pass
