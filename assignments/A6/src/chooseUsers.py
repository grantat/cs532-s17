import json
import csv
import random


def chooseUsers():
    data = []
    totalLines = sum(1 for line in open('data/phonedudeFollowers.json'))
    randUsers = random.sample(range(1, totalLines), 100)

    with open('data/phonedudeFollowers.json') as f:
        for i, line in enumerate(f):
            if i in randUsers:
                data.append(json.loads(line))

    # save selected json followers to file
    with open('data/chosenFollowers.json','w') as f:
        for i in data:
            # print(i,file=f)
            print(json.dumps(i),file=f)
            print(i["name"])

    # save selected fields to csv
    writeCSV(data,"data/chosenFollowers.csv")


def writeCSV(data, filename):
    with open(filename, 'w', newline='') as file:
        for d in data:
            writer = csv.writer(file, delimiter=',')
            row = [d["name"], d["screen_name"], d["profile_image_url"]]
            writer.writerow(row)


if __name__ == "__main__":
    chooseUsers()