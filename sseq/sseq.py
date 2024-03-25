import logging
import sys

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
# logging.disable(logging.CRITICAL)

if __name__ == "__main__":

    filename = sys.argv[1]
    dnaString = ""
    dnaSubstring = ""
    with open(filename, 'r') as f:
        count = 0
        for line in f:
            line = line.strip()
            if line[0] == '>':
                count += 1
                continue

            if count == 1:
                dnaString += line
            else:
                dnaSubstring += line

    logging.debug(dnaString)
    logging.debug(dnaSubstring)

    indices = []
    index = 0
    for i in range(len(dnaString)):
        if dnaString[i] == dnaSubstring[index]:
            indices.append(i+1)
            index += 1

        if index == len(dnaSubstring):
            break

    with open('output.txt', 'w') as f:
        f.write(' '.join([str(x) for x in indices]))