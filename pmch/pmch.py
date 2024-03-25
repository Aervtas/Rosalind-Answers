import logging
import sys
import math

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
# logging.disable(logging.CRITICAL)

if __name__ == "__main__":

    rnaString = ""
    filename = sys.argv[1]
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if line[0] == '>':
                logging.debug(line)
            else:
                rnaString += line

    # Bonding Graph Algorithm
    # First assign each symbol of the rna string to a node
    # Arrange the nodes in a ring connected with adjacency edges
    # Form all possible basepair edges [A, U] and [C, G]
    # this actually means that you get the factorial of number of 'A' or 'U' times
    # the factorial of number of 'C' or 'G'

    aNum = 0
    cNum = 0
    for x in rnaString:
        if x == 'A':
            aNum += 1
        elif x == 'C':
            cNum += 1

    res = math.factorial(aNum) * math.factorial(cNum)
    logging.debug(str(res))

    with open('pmch.out', 'w') as f:
        f.write(str(res))