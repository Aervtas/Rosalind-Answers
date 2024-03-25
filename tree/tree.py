import logging
import sys

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
# logging.disable(logging.CRITICAL)

if __name__ == "__main__":

    filename = sys.argv[1]
    n = 0
    connectedNode = []
    singletons = []
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip().split()
            if len(line) == 1:
                n = int(line[0])
                singletons = list(map(str, range(1, n + 1)))
            else:

                if line[0] in singletons:
                    singletons.remove(line[0])
                if line[1] in singletons:
                    singletons.remove(line[1])

                # logging.debug(singletons)
                # add nodes to connectedNode and merge sets if line[0] and line[1] are in the different sets
                check = 0
                merge = []
                for i in range(len(connectedNode)):
                    if line[0] in connectedNode[i]:
                        connectedNode[i].add(line[1])
                        check += 1
                        merge.append(i)
                    elif line[1] in connectedNode[i]:
                        connectedNode[i].add(line[0])
                        check += 1
                        merge.append(i)

                # If line[0] and line[1] are in the same set, merge the sets
                if check > 1:
                    logging.debug(merge)
                    tempSet = set()
                    for i in range(len(merge), 0, -1):
                        tempSet = tempSet.union(connectedNode.pop(merge[i - 1]))
                        
                    connectedNode.append(tempSet)

                # If line[0] and line[1] are not in collection yet
                if not check:
                    connectedNode.append(set(line))

    # logging.debug(connectedNode)

    
    res = len(singletons) + len(connectedNode) - 1
    logging.debug(len(singletons))
    logging.debug(len(connectedNode))
    print(res)

    with open('output.txt', 'w') as f:
        f.write(str(connectedNode))