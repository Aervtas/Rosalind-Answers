import logging
import sys
import math

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
# logging.disable(logging.CRITICAL)

filename = sys.argv[1]
n = 0
k = 0
with open(filename, 'r') as f:
    k, n = f.read().strip().split()
logging.debug("N: "+n+"  K: "+k)
n = int(n)
k = int(k)

children = 2**k
resProb = 1
for i in range(children - n + 1, children + 1):
    logging.debug("i: "+str(i))
    resProb -= (0.25 ** (children - i)) * (0.75 ** i) * math.comb(children, i) 

print(resProb)