import logging
import sys

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
# logging.disable(logging.CRITICAL)

filename = sys.argv[1]

with open(filename, 'r') as f:
    s = f.readline().strip()
    t = f.readline().strip()

    hdistance = 0

    for stmp, ttmp in zip(s, t):
        if stmp != ttmp:
            hdistance += 1
    
    print(hdistance)