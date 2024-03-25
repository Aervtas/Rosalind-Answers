import logging
import sys

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

with open(sys.argv[1]) as f:
    data = f.read()

data = data.split()
k, m, n = data
k = int(k)
m = int(m)
n = int(n)
population = k + m + n
pop2 = population - 1
logging.debug(population)

kprob = (k / population) * ((k - 1) /  pop2)
kprob += (k / population) * (m / pop2)
kprob += (k / population) * (n / pop2)
logging.debug(kprob)

mprob = (m / population) * (k / pop2)
mprob += (m / population) * ((m - 1) / pop2) * 0.75
mprob += (m / population) * (n / pop2) * 0.5
logging.debug(mprob)

nprob = (n / population) * (k / pop2)
nprob += (n / population) * (m / pop2) * 0.5
logging.debug(nprob)

res = kprob + mprob + nprob
print(round(res, 5))