import logging
import sys
import json

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
# logging.disable(logging.CRITICAL)

tableDict = json.load(open("monoisotopic_mass_table.json", 'r'))
filename = sys.argv[1]

protString = ""
with open(filename, 'r') as f:
    protString = f.read().strip()

res = 0
for x in protString:
    res += tableDict[x]

print(res)