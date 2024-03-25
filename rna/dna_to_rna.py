import logging
import sys

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

with open(sys.argv[1]) as f:
    data = f.read()

for x in data:
    if x == 'T':
        print('U', end = '')
    else:
        print(x, end = '')