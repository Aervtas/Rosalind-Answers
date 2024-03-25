import logging
import sys

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
# logging.disable(logging.CRITICAL)

if __name__ == "__main__":

    substringCandidates = set()
    dnaSeq = []

    filename = sys.argv[1]
    with open(filename, 'r') as f:
        tempSeq = ""
        for row in f:
            string = row.strip()
            if string[0] == '>':
                if len(tempSeq) > 0:
                    dnaSeq.append(tempSeq)
                tempSeq = ""
                continue
            else:
                tempSeq += string

        if len(tempSeq) > 0:
            dnaSeq.append(tempSeq)

    # Edge case return the only sequence
    if len(dnaSeq) == 1:
        with open('output.txt', 'w') as f:
            f.write(dnaSeq[0])
        exit()

    firstSeq = dnaSeq[0]
    secondSeq = dnaSeq[1]

    # sliding window of firstSeq and secondSeq to find substring candidates
    for i in range(len(firstSeq) - 2):
        temp = ""
        for j in range(len(secondSeq)):
            if i + j >= len(firstSeq):
                if len(temp) > 0:
                    substringCandidates.add(temp)
                break

            if firstSeq[i + j] == secondSeq[j]:
                temp += firstSeq[i + j]
            elif len(temp) > 0:
                substringCandidates.add(temp)
                temp = ""

    for i in range(len(secondSeq) - 2):
        temp = ""
        for j in range(len(firstSeq)):
            if i + j >= len(secondSeq):
                if len(temp) > 0:
                    substringCandidates.add(temp)
                break

            if secondSeq[i + j] == firstSeq[j]:
                temp += secondSeq[i + j]
            elif len(temp) > 0:
                substringCandidates.add(temp)
                temp = ""

    # loop through subsequent dna sequences to begin removing substring candidates
    for sequence in dnaSeq[2:]:
        for candidate in list(substringCandidates):
            if candidate not in sequence:
                substringCandidates.remove(candidate)

    logging.debug(substringCandidates)

    with open('output.txt', 'w') as f:
        longest_substring = ''
        for candidate in substringCandidates:
            if len(candidate) > len(longest_substring):
                longest_substring = candidate
        f.write(longest_substring + '\n')
