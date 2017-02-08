#!/usr/bin/env python3

import requests
import os
import json
import csv


def saveOutput(uri,count):

    if not os.path.exists("output"):
        os.makedirs("output")

    # Save json received/created to output
    fields = [uri,count]
    # try:
    #     with open('output/timeMaps.csv', 'a', newline='') as file:
    #         writer = csv.writer(file, delimiter=',')
    #         writer.writerow(fields)
    # except (IOError, ValueError):
    #     with open('output/timeMaps.csv', 'w', newline='') as file:
    #         writer = csv.writer(file, delimiter=',')
    #         writer.writerow(fields)


def countMementos(jsonResp):
    try:
        data = json.loads(jsonResp)
        count = len(data["mementos"]["list"])
        return count
    except:
        return 0



with open("output/finalURIs.txt", "r") as file:
    lines = file.readlines()
    for num, line in enumerate(lines):
        try:
            timeMapURI = "http://memgator.cs.odu.edu/timemap/json/" + line
            print(timeMapURI)
            resp = requests.get(timeMapURI, stream=True, allow_redirects=True, headers={
                                'User-Agent': 'Mozilla/5.0'})

            if resp.status_code == 200:
                # count through json arr
                print(resp.text)
                count = countMementos(resp.text)
                saveOutput(line,count)
                if count > 2:
                    exit()
            else:
                count = 0
                saveOutput(line,count)

        except KeyboardInterrupt:
            print()
            exit()
        except:
            pass
