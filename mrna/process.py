import json
    
mydict = json.load(open("rna_codon.json", 'r'))

newdict = {}

for x in mydict.values():
    if x in newdict.keys():
        newdict[x] += 1
    else:
        newdict[x] = 1

json.dump(newdict,open("protein_freq.json", 'w'))