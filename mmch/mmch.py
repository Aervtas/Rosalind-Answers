import logging
import sys
import math

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
# logging.disable(logging.CRITICAL)

def factorial(n):
    """
    Calculate the factorial of n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def comb(n, k):
    return factorial(n) // factorial(n-k)

if __name__ == "__main__":

    filename = sys.argv[1]
    rnaString = ''
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if line[0] == '>':
                continue
            else:
                rnaString += line

    logging.debug(rnaString)

    aNum = 0
    uNum = 0
    cNum = 0
    gNum = 0
    for x in rnaString:
        match x:
            case 'A':
                aNum += 1
            case 'U':
                uNum += 1
            case 'C':
                cNum += 1
            case 'G':
                gNum += 1

    # What is a maximum matching?
    # It is the largest number of nodes that can be matched
    # Therefor you would take A times U, C times G then calculate the combinations of the 2

    logging.debug(str(aNum) + " " + str(uNum) + " " + str(cNum) + " " + str(gNum))
    result = comb(aNum, uNum) * comb(cNum, gNum)
    logging.debug(str(result))
