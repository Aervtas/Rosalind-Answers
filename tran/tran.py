import logging
import sys

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
# logging.disable(logging.CRITICAL)

if __name__ == "__main__":

    filename = sys.argv[1]
    dnaString1 = ""
    dnaString2 = ""
    with open(filename, 'r') as f:
        count = 0
        for line in f:
            line = line.strip()
            if line[0] == '>':
                count += 1
                continue

            if count == 1:
                dnaString1 += line
            elif count == 2:
                dnaString2 += line

    transitionCount = 0
    transversionCount = 0
    for a, b in zip(dnaString1, dnaString2):
        if a == b:
            continue
        elif a in ['A', 'G'] and b in ['A', 'G']:
            transitionCount += 1
        elif a in ['C', 'T'] and b in ['C', 'T']:
            transitionCount += 1
        else:
            transversionCount += 1

    print(transitionCount/transversionCount)