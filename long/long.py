import logging
import sys

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
# logging.disable(logging.CRITICAL)

def compareOverlap(s1, s2):
    length = len(s1)
    half = (length + 1) // 2
    for i in range(half, length):
        if s1[-1 * i:] == s2[:i]:
            return i

    return -1

if __name__ == "__main__":

    filename = sys.argv[1]
    dnaStrings = []
    with open(filename, 'r') as f:
        count = -1
        for line in f:
            line = line.strip()
            if line[0] == '>':
                count += 1
                dnaStrings.append("")
            else:
                dnaStrings[count] += line

    

    # Each of the entries to be combined will overlap by more than half the length of the string
    
    overlapList = []
    for i in range(len(dnaStrings)):
        # logging.debug(dnaList)
        for j in range(len(dnaStrings)):
            if i == j:
                continue
            frontOverlap = compareOverlap(dnaStrings[j], dnaStrings[i])
            backOverlap = compareOverlap(dnaStrings[i], dnaStrings[j])
            if backOverlap > 0:
                if (backOverlap, i, j) not in overlapList:
                    overlapList.append((backOverlap, i, j))
            if frontOverlap > 0:
                if (frontOverlap, j, i) not in overlapList:
                    overlapList.append((frontOverlap, j, i))

    logging.debug(overlapList)
    logging.debug(len(overlapList))
    logging.debug(list(filter(lambda x: x[1] == 100, overlapList)))

    conflict = {}
    for a, b, c in overlapList:
        if b not in conflict.keys():
            conflict[b] = c
        elif c == conflict[b]:
            continue
        else:
            logging.debug(b + " " + conflict[b] + " " + c)

    a, left, right = overlapList.pop(0)
    res = dnaStrings[left] + dnaStrings[right][a:]
    logging.debug(res)
    while len(overlapList) > 0:
        # Get the right and left strings and append them
        # If they don't exist then skip
        
        tempRight = list(filter(lambda x: x[1] == right, overlapList))
        tempLeft = list(filter(lambda x: x[2] == left, overlapList))
        print(tempLeft, tempRight)
        if tempLeft == [] and tempRight == []:
            break
        if len(tempRight) > 0:
            a, b, c = tempRight[0]
            res += dnaStrings[c][a:]
            right = c
            # print(res)
            overlapList.remove(tempRight[0])
        if len(tempLeft) > 0:
            a, b, c = tempLeft[0]
            res = dnaStrings[b][: -1 * a] + res
            left = b
            # print(res)
            overlapList.remove(tempLeft[0])

    print(overlapList)
    with open("output.txt", "w") as f:
        f.write(res)
