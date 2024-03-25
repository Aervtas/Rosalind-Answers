import logging
import sys

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

with open(sys.argv[1]) as f:
    data = f.read()

n, k = data.split()
n = int(n)
k = int(k)

prev1 = 1
prev2 = 1
for i in range(n - 2):
    temp = (prev1 * k) + prev2
    prev1 = prev2
    prev2 = temp

print(prev2)