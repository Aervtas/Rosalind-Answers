import logging
import sys

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
# logging.disable(logging.CRITICAL)

filename = sys.argv[1]

myDict = {}

with open(filename, 'r') as f:
    temp = ''
    for row in f:
        if row[0] == '>':
            temp = row.strip()[1:]
            myDict[temp] = ''
        else:
            myDict[temp] = myDict[temp] + row.strip()

with open("output.txt", 'w') as f:
    for key in myDict.keys():
        for compKey in myDict.keys():
            if compKey != key and myDict[key] != myDict[compKey]:
                if myDict[key][-3:] == myDict[compKey][:3]:
                    f.write(key + ' ' + compKey + '\n')