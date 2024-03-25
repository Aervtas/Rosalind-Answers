import logging
import sys

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
# logging.disable(logging.CRITICAL)

if __name__ == "__main__":

    filename = sys.argv[1]
    reverseComplement = ""
    dnaString = ""

    with open(filename, 'r') as f:
        for row in f:
            row = row.strip()
            if row[0] == '>':
                continue
            else:
                dnaString += row

    for x in dnaString:
        match x:
            case 'A':
                reverseComplement = reverseComplement + 'T'
            case 'T':
                reverseComplement = reverseComplement + 'A'
            case 'C':
                reverseComplement = reverseComplement + 'G'
            case 'G':
                reverseComplement = reverseComplement + 'C'


    logging.debug(dnaString)
    logging.debug(reverseComplement)
    
    # Sliding window to find matches between 4 and 12 in length
    indices = []
    lengths = []

    logging.debug(dnaString[:4])
    logging.debug(reverseComplement[-4:])

    for i in range(len(dnaString) - 3):
        for j in range(4, 13):
            logging.debug(dnaString[i:i+j])
            logging.debug(reverseComplement[i:i+j][::-1])
            if j > len(dnaString) - i:
                break
            if dnaString[i:i+j] == reverseComplement[i:i+j][::-1]:
                indices.append(i + 1)
                lengths.append(j)
                
    logging.debug(indices)
    logging.debug(lengths)

    with open(filename[:-4]+"_output.txt", 'w') as outfile:
        for i in range(len(indices)):
            outfile.write(str(indices[i]) + " " + str(lengths[i]) + "\n")

    