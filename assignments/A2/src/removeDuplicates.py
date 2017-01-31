#!/usr/bin/env python3


# remove duplicates - stackoverflow post

removedLines = []

# finalURIs
with open("output/finalURIs.txt", "r+") as file:
    lines = file.readlines()
    uniqueLines = set()
    for num, line in enumerate(lines):
        if line not in uniqueLines:
            uniqueLines.add(line)
        else:
            print(num, "Line Removed:", line)
            removedLines.append(num)
            # list.remove removes first occurence, so del[i] is needed
            del lines[num]
    file.truncate(0)         # truncates the file
    file.seek(0)             # moves the pointer to the start of the file
    file.writelines(lines)   # write the new data to the file


# remove from originalURIs as well
with open("output/originalURIs.txt","r+") as file:
    lines = file.readlines()
    for num,line in enumerate(lines):
        for badLineNum in removedLines:
            if num == badLineNum:
                print(badLineNum,"Line Removed:",line)
                lines.remove(line)
                break
    file.truncate(0)         # truncates the file
    file.seek(0)             # moves the pointer to the start of the file
    file.writelines(lines)   # write the new data to the file
