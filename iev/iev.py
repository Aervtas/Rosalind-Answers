import logging
import sys

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
# logging.disable(logging.CRITICAL)

filename = sys.argv[1]

with open(filename, 'r') as f:
    populationData = f.read().strip()
    populationData = populationData.split()
    populationData = list(map(int, populationData))

    total = populationData[0] * 2
    total += populationData[1] * 2
    total += populationData[2] * 2
    total += populationData[3] * 1.5
    total += populationData[4]
    
    print(total)