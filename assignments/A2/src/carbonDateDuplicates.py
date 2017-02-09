import csv

# This was a fix for carbonDate original. Some were duplicated
with open('output/carbonDate.csv', 'r') as in_file, open('output/carbonDate2.csv', 'w') as out_file:
    csvdict = {}
    spamreader = csv.reader(in_file, delimiter=',')
    for row in spamreader:
        key = row[0]
        if (key in csvdict) == False:
        # if key not in seen and row[1] != "":
            csvdict[row[0]] = row[1]
        elif key in csvdict and row[1] != "":
            csvdict[row[0]] = row[1]


    writer = csv.writer(out_file, delimiter=',')
    for key, value in csvdict.items():
       writer.writerow([key, value])
    

