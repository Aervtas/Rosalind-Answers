import logging
import sys

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
# logging.disable(logging.CRITICAL)

def permute(nList, n):
    if n == 1:
        return nList
    else:
        aggregateList = []
        for i in range(len(nList)):
            for x in permute(nList, n-1):
                aggregateList += [nList[i] + x]
        return aggregateList

if __name__ == "__main__":

    filename = sys.argv[1]
    alphabet = []
    n = 0
    with open(filename, 'r') as f:
        alphabet = f.readline().strip().split()
        n = int(f.readline().strip())
    
    res = permute(alphabet, n)
    res.sort()
    logging.debug(res)
    logging.debug(len(res))

    with open('output.txt', 'w') as f:
        for i in range(len(res)):
            f.write(res[i] + '\n')