import logging
import sys

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

with open(sys.argv[1]) as f:
    data = f.read()

numA = 0
numC = 0
numG = 0
numT = 0

logging.debug(data)

for x in data:
    if x == 'A':
        numA += 1
    elif x == 'C':
        numC += 1
    elif x == 'G':
        numG += 1
    elif x == 'T':
        numT += 1

print(str(numA) + " " + str(numC) + " " + str(numG) + " " + str(numT))