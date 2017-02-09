#!/usr/bin/env python3

import requests
import os
import json
import csv
import datetime

def saveOutput(uri,estDate):

    if not os.path.exists("output"):
        os.makedirs("output")

    # Save json received/created to output
    fields = [uri,estDate]
    try:
        with open('output/carbonDate.csv', 'a', newline='') as file:
            writer = csv.writer(file, delimiter=',')
            writer.writerow(fields)
    except (IOError, ValueError):
        with open('output/carbonDate.csv', 'w', newline='') as file:
            writer = csv.writer(file, delimiter=',')
            writer.writerow(fields)


def getJson(jsonResp):
    data = json.loads(jsonResp)
    estDate = data["Estimated Creation Date"]
    return estDate


startFlag = False
with open("output/finalURIs.txt", "r") as file:
    lines = file.readlines()
    for num, line in enumerate(lines):
        if startFlag == True or 'http://www.reviewjournal.com/neon/arts-culture/dave-loeb-brings-jazz-music-las-vegas' in line:
            startFlag = True
            # saveOutput(line,"")
            try:
                carbonDateURI = "http://localhost:8888/cd?url=" + line
                print(carbonDateURI)
                resp = requests.get(carbonDateURI, stream=True, allow_redirects=True, headers={
                                    'User-Agent': 'Mozilla/5.0'})

                if resp.status_code == 200:
                    # count through json arr
                    print(resp.text)

                    estDate = getJson(resp.text)
                    saveOutput(line,estDate)
                else:
                    estDate = ""
                    saveOutput(line,estDate)

            except KeyboardInterrupt:
                print()
                exit()
            except:
                pass
