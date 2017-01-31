#!/usr/bin/env python3

# unwanted domainsw
blacklist = ['.xyz','.pw','http://artist-rack.com?']
# track lines removed from finalURIs for originalURIs
removedLines = []
artistRackFlag = False


# Remove unwanted from finalURIs
with open("output/finalURIs.txt","r+") as file:
    lines = file.readlines()
    for num,line in enumerate(lines):
        for f in blacklist:
            if f in line:
                if f in 'http://artist-rack.com?' and artistRackFlag == False:
                    artistRackFlag = True
                    break
                else:
                    removedLines.append(num)
                    lines.remove(line)
                    print(num,"type found:",f,":",line)
                    break
            elif 'youtube.com' in line and '&' in line:
                pos = line.find('&')
                finalURI = line[:pos]
                print("FINALURI:",finalURI)
                lines[num] = finalURI+"\n"
                break
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


