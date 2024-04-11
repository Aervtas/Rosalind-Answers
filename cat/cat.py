#!/usr/bin/env python3
import logging
import sys

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
# logging.disable(logging.CRITICAL)

def expandCatalan(cNums, n):
    pass

if __name__ == "__main__":

    # Process the RNA string first
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

    # Catalan Numbers
    # For points {i, j} and {k, l} they are not crossing if i < k < j < l
    # C_0 = 1 and C_1 = 1 because there is only one way to arrange 0 and 1 node
    # Complete graph is K_2n
    # m is to vary over all possible n - 1 choices between 1 and 2n (2n is basically representing all even numbers)
    # then sum up every possibility of m and return the result
    # the additional conditions when applied to rna are the following
    # - Not every even number is can bond with node 1 (A <> U and C <> G)
    # - Not every slice of (1, m) can match perfectly depending on number of AUCG's in the slice
    # - The matches in the slice also have to be noncrossing
    # - This makes each subslice its own noncrossing perfect matching problem
    # - If any of the above conditions are not met, that m can be immediately discarded

    # So if index-0 is 1 then m has to start from 1,3,5 and so on, so there are an even number of nodes trapped under the first slice