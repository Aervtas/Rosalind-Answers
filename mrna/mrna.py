import logging
import sys
import json

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
# logging.disable(logging.CRITICAL)

filename = sys.argv[1]

protDict = json.load(open('protein_freq.json', 'r'))

res = 1
proteinString = ""
with open(filename, 'r') as f:
    proteinString = f.read().strip()

for x in proteinString:
    res = (protDict[x] * res) % 1000000

res = (res * 3) % 1000000 # 3 is for the possible stop codons that don't show up

print(res)