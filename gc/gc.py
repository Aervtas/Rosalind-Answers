import logging
import sys

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)
with open(sys.argv[1]) as f:
    topRes = 0.0
    topEntry = ""
    recentEntry = ""
    recentTotal = 0
    recentGC = 0

    for rawdata in f:
        data = rawdata.strip()
        if data[0] == '>':

            if recentTotal != 0:
                logging.debug(str(recentGC) + " / " + str(recentTotal) + " : " + str(recentGC /  recentTotal))
                logging.debug(data)
                if (recentGC /  recentTotal) > topRes:
                    topEntry = recentEntry
                    topRes = (recentGC /  recentTotal)

            recentEntry = data
            recentTotal = 0
            recentGC = 0
        else:
            for x in data:
                if x == 'G' or x == 'C':
                    recentGC += 1
                recentTotal += 1

    logging.debug(str(recentGC) + " / " + str(recentTotal) + " : " + str(recentGC /  recentTotal))
    if (recentGC /  recentTotal) > topRes:
        topEntry = recentEntry
        topRes = (recentGC /  recentTotal)

    print(topEntry[1::])
    print(round(topRes * 100, 7))