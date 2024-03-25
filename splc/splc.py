import logging
import sys
import json

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
# logging.disable(logging.CRITICAL)

if __name__ == "__main__":

    dnaString = ""
    exonList = []
    dnaDict = json.load(open('dna_codon.json', 'r'))
    filename = sys.argv[1]
    with open(filename, 'r') as f:
        line = 0
        for row in f:
            string = row.strip()
            if string[0] == '>':
                line += 1
                continue
            
            if line == 1:
                dnaString += string
            else:
                exonList.append(string)

    logging.debug(dnaString)
    logging.debug(exonList)

    index = 0
    while index < len(dnaString):
        for exon in exonList:
            if dnaString[index:index+len(exon)] == exon:
                dnaString = dnaString[:index] + dnaString[index+len(exon):]
        index += 1

    with open("output.txt", 'w') as f:
        for i in range(0, len(dnaString), 3):
            if dnaDict[dnaString[i:i+3]] == 'Stop':
                continue
            f.write(dnaDict[dnaString[i:i+3]])