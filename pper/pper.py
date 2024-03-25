import logging
import sys

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
# logging.disable(logging.CRITICAL)

if __name__ == "__main__":

    filename = sys.argv[1]
    n = 0
    k = 0
    with open(filename, 'r') as f:
        n, k = f.read().strip().split()
    n = int(n)
    k = int(k)

    res = 1
    for i in range(k):
        logging.debug(str(res))
        res *= (n - i)

        res %= 1000000

    logging.debug(res)
    with open("output.txt", 'w') as f:
        f.write(str(res))