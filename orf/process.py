import json

dnaDict = {}
rnaDict = {}
with open('rna_codon.json', 'r') as f:
    jsonData = f.read()
    rnaDict = json.loads(jsonData)
    for x in rnaDict.keys():
        temp = x.replace('U', 'T')
        dnaDict[temp] = rnaDict[x]

with open('dna_codon.json', 'w') as f:
    json.dump(dnaDict, f)