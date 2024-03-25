import logging
import sys
from enum import Enum

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
# logging.disable(logging.CRITICAL)

filename = sys.argv[1]

# Enum for the 4 amino acids A, C, G, T corresponding to 0, 1, 2, 3from enum import Enum

class AminoAcid(Enum):
    A = 0
    C = 1
    G = 2
    T = 3

resString = ""
profileMatrix = [[], [], [], []]

with open(filename, 'r') as f:
    entry = 0
    index = 0
    for row in f:
        row = row.strip()
        if row[0] == '>':
            entry += 1
            index = 0
        elif entry == 1:
            for i, x in enumerate(row):
                match x:
                    case 'A':
                        profileMatrix[AminoAcid.A.value].append(1)
                        profileMatrix[AminoAcid.C.value].append(0)
                        profileMatrix[AminoAcid.G.value].append(0)
                        profileMatrix[AminoAcid.T.value].append(0)
                    case 'C':
                        profileMatrix[AminoAcid.A.value].append(0)
                        profileMatrix[AminoAcid.C.value].append(1)
                        profileMatrix[AminoAcid.G.value].append(0)
                        profileMatrix[AminoAcid.T.value].append(0)
                    case 'G':
                        profileMatrix[AminoAcid.A.value].append(0)
                        profileMatrix[AminoAcid.C.value].append(0)
                        profileMatrix[AminoAcid.G.value].append(1)
                        profileMatrix[AminoAcid.T.value].append(0)
                    case 'T':
                        profileMatrix[AminoAcid.A.value].append(0)
                        profileMatrix[AminoAcid.C.value].append(0)
                        profileMatrix[AminoAcid.G.value].append(0)
                        profileMatrix[AminoAcid.T.value].append(1)
        elif entry >= 2:
            for x in row:
                profileMatrix[AminoAcid[x].value][index] += 1
                index += 1

# loop through length of profileMatrix[0] to get the largest value in each column and append the corresponding amino acid to resString
for i in range(len(profileMatrix[0])):
    maxVal = max(profileMatrix[0][i], profileMatrix[1][i], profileMatrix[2][i], profileMatrix[3][i])
    if maxVal == profileMatrix[0][i]:
        resString += 'A'
    elif maxVal == profileMatrix[1][i]:
        resString += 'C'
    elif maxVal == profileMatrix[2][i]:
        resString += 'G'
    elif maxVal == profileMatrix[3][i]:
        resString += 'T'

with open('output.txt', 'w') as f:
    f.write(resString)
    f.write("\nA: " + ' '.join(map(str, profileMatrix[0])))
    f.write("\nC: " + ' '.join(map(str, profileMatrix[1])))
    f.write("\nG: " + ' '.join(map(str, profileMatrix[2])))
    f.write("\nT: " + ' '.join(map(str, profileMatrix[3])))
