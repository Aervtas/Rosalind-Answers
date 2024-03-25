#!/usr/bin/env python3
import logging
import sys
import math

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
# logging.disable(logging.CRITICAL)

if __name__ == "__main__":

    filename = sys.argv[1]
    n = 0
    with open(filename, 'r') as f:
        n = int(f.readline().strip())
    
    logging.debug(n)

    totalSubsets = 0
    for i in range(1, n+1):
        totalSubsets += math.comb(n, i)
        totalSubsets %= 1000000

    totalSubsets += 1 # Include empty set

    print(totalSubsets)