#!/usr/bin/env python3
import logging
import sys

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
# logging.disable(logging.CRITICAL)

def catalanNum(n):
    if n == 0 or n == 1:
        return 1
    else:
        return (4 * n - 2) * catalanNum(n - 1) / (n + 1)

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

