import logging
import sys

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
# logging.disable(logging.CRITICAL)

def permute(nList, n):
    if n == 0:
        return [[]]
    else:
        aggregateList = []
        for i in range(len(nList)):
            for x in permute(nList[:i] + nList[i+1:], n-1):
                aggregateList += [[nList[i]] + x]
                aggregateList += [['-'+nList[i]] + x]
        return aggregateList

if __name__ == "__main__":

    filename = sys.argv[1]
    n = 0
    with open(filename, 'r') as f:
        n = int(f.read().strip())

    nExpanded = [str(x) for x in range(1, n+1)]
    logging.debug(nExpanded)
    resList = permute(nExpanded, n)
    logging.debug(resList)


    with open('output.txt', 'w') as f:
        f.write(str(len(resList)) + '\n')
        for i in range(len(resList)):
            f.write(' '.join(map(str, resList[i])) + '\n')

