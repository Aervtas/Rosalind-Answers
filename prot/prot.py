import logging
import sys
import json

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
# logging.disable(logging.CRITICAL)

codonDict = {}

with open('rna_codon.json', 'r') as f:
    jsonData = f.read()
    codonDict = json.loads(jsonData)

with open(sys.argv[1]) as f:
    rnaString = f.read().strip()
    resultString = ""

    for i in range(0, len(rnaString), 3):
        if codonDict[rnaString[i:i+3]] != 'Stop':
            resultString += codonDict[rnaString[i:i+3]]

    print(resultString)