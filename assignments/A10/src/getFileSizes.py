import os
import csv

savefile = open('data/new_processed_size', 'w')
path = "data/processed"

for filename in os.listdir(path):
    filepath = os.path.join(path, filename)
    size = os.path.getsize(filepath)
    savefile.write(filename + "|" + str(size))
    savefile.write('\n')
    print(size)

savefile = open('data/new_raw_size', 'w')
path = "data/html"

for filename in os.listdir(path):
    filepath = os.path.join(path, filename)
    size = os.path.getsize(filepath)
    savefile.write(filename + "|" + str(size))
    savefile.write('\n')
    print(size)

savefile = open('data/old_processed_size', 'w')
path = "../../A3/src/output/processed"

for filename in os.listdir(path):
    filepath = os.path.join(path, filename)
    size = os.path.getsize(filepath)
    savefile.write(filename + "|" + str(size))
    savefile.write('\n')
    print(size)

savefile = open('data/old_raw_size', 'w')
path = "../../A3/src/output/html"

for filename in os.listdir(path):
    filepath = os.path.join(path, filename)
    size = os.path.getsize(filepath)
    savefile.write(filename + "|" + str(size))
    savefile.write('\n')
    print(size)

# merge raw file counts
with open('data/new_raw_size', 'r') as f, open("data/old_raw_size", 'r') as f2, open("data/mergedRaw", 'w') as out:
    reader = csv.reader(f, delimiter="|")
    reader2 = csv.reader(f2, delimiter="|")
    l1 = list(reader)
    l2 = list(reader2)
    for i in l1:
        filename = i[0]
        for j in l2:
            oldfile = j[0]
            if filename == oldfile:
                # diff
                sizeDiff = int(i[1]) - int(j[1])
                out.write(filename + "|" + str(sizeDiff))
                out.write("\n")

# merge processed counts
with open('data/new_processed_size', 'r') as f, open("data/old_processed_size", 'r') as f2, open("data/mergedProccessed", 'w') as out:
    reader = csv.reader(f, delimiter="|")
    reader2 = csv.reader(f2, delimiter="|")
    l1 = list(reader)
    l2 = list(reader2)
    for i in l1:
        filename = i[0]
        for j in l2:
            oldfile = j[0]
            if filename == oldfile:
                # diff
                sizeDiff = int(j[1]) - int(i[1])
                out.write(filename + "|" + str(sizeDiff))
                out.write("\n")
