import logging
import sys

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
# logging.disable(logging.CRITICAL)

filename = sys.argv[1]

with open(filename, 'r') as f:
    nums = f.read().strip().split()
    n = int(nums[0]) # Months of breeding
    m = int(nums[1]) # Months before death

    deathQueue = [0] * m
    deathQueue[0] = 1
    for i in range(n - 1):
        logging.debug(str(i)+": "+str(deathQueue))
        newPop = sum(deathQueue[1:])
        deathQueue.pop(-1)
        deathQueue.insert(0, newPop)
        
    print(sum(deathQueue))