import logging
import sys

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
# logging.disable(logging.CRITICAL)

filename = sys.argv[1]

with open(filename, 'r') as f:
    t = f.readline().strip()
    s = f.readline().strip()
    logging.debug(s)
    tlen = len(t)
    slen = len(s)
    logging.debug(str(tlen)+" "+str(slen))
    for i in range(0, tlen - slen):
        if t[i:i+slen] == s:
            print(str(i+1)+" ")