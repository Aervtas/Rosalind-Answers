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

    internalNodes = 1
    n -= 3
    internalNodes += n

    print(internalNodes)