import logging
import sys

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
# logging.disable(logging.CRITICAL)

def permute(nList):
    if len(nList) == 1:
        return [nList]
    else:
        aggregateList = []
        for i in range(len(nList)):
            for x in permute(nList[:i] + nList[i+1:]):
                aggregateList += [[nList[i]] + x]
        return aggregateList

if __name__ == "__main__":

    filename = sys.argv[1]
    num = 0

    with open(filename, 'r') as f:
        num = int(f.read().strip())

    # expand numbers from 1 to num into a list while casting to str
    numList = [str(x) for x in range(1, num+1)]

    logging.debug(numList)
    permArray = permute(numList)

    logging.debug(permArray)

    with open('output.txt', 'w') as f:
        f.write(str(len(permArray)) + '\n')

        for i in range(len(permArray)):
            f.write(' '.join(permArray[i]) + '\n')
        