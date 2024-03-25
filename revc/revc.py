import logging
import sys

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

with open(sys.argv[1]) as f:
    data = f.read()

res = ""

for x in data:
    if x == 'A':
        res = 'T' + res
    elif x == 'G':
        res = 'C' + res
    elif x == 'C':
        res = 'G' + res
    elif x == 'T':
        res = 'A' + res


with open('output.txt', 'w') as textdoc:
    textdoc.write(res)