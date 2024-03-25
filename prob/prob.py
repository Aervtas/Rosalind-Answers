import logging
import sys
import math

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
# logging.disable(logging.CRITICAL)

if __name__ == "__main__":

    filename = sys.argv[1]
    dnaString = ""
    aList = []
    with open(filename, 'r') as f:
        dnaString = f.readline().strip()
        aList = f.readline().strip().split()
    aList = list(map(float, aList))

    bList = []
    for x in aList:
        gc = x/2
        at = (1-x)/2
        temp = 1.0
        for y in dnaString:
            if y == 'C' or y == 'G':
                temp *= gc
            else:
                temp *= at
        bList.append(temp)

    bList = ['{0:0<6.3f}'.format(round(math.log10(x), 3)) for x in bList]

    with open('output.txt', 'w') as f:
        f.write(' '.join(bList))