import csv
import os
import datetime


def findDays(datePassed):
    try:
        now = datetime.datetime.today()
        datePassed = datetime.datetime.strptime(datePassed, "%Y-%m-%dT%H:%M:%S")
        days = (now - datePassed).days
        return days
    except:
        return ""


def mergeCSVs():

    if not os.path.exists("output"):
        os.makedirs("output")

    desiredRows = []

    # Save json received/created to output
    with open('output/timeMaps.csv', 'r',newline='') as timeMaps, open('output/carbonDate.csv', 'r',newline='') as carbonDates:
        
        reader = csv.reader(timeMaps)
        reader2 = csv.reader(carbonDates)

        for row in reader:
            temp = []
            temp.append(row[0])
            temp.append(row[1])
            for row2 in reader2:
                if(row[0] == row2[0]):
                    days = findDays(row2[1])
                    temp.append(days)
                    break
            
            desiredRows.append(temp)

    with open('output/carbonDateMerged.csv', 'w', newline='') as file:
        for row in desiredRows:
            writer = csv.writer(file, delimiter=',')
            writer.writerow(row)


mergeCSVs()