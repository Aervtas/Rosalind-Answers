import json

codonDict = {}

with open('rna_codon.txt', 'r') as f:
    for rowData in f:
        rowData = rowData.split()
        for i in range(0, len(rowData), 2):
            codonDict[rowData[i]] = rowData[i+1]

with open('rna_codon.json', 'w') as f:
    json.dump(codonDict, f)