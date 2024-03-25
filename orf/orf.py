import logging
import sys
import json
import concurrent.futures

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
# logging.disable(logging.CRITICAL)


def template_function(input_string):
    candidate_proteins = []

    for i in range(len(input_string) - 3):
        if dnaDict[input_string[i:i+3]] == 'M':
            tempCandidate = ''
            for j in range(i, len(input_string), 3):
                if len(input_string[j:j+3]) != 3:
                    break
                if dnaDict[input_string[j:j+3]] == 'Stop':
                    candidate_proteins.append(tempCandidate)
                    break
                tempCandidate += dnaDict[input_string[j:j+3]]
                
    return candidate_proteins

if __name__ == "__main__":

    filename = sys.argv[1]
    dnaDict = json.load(open('dna_codon.json', 'r'))
    dnaString = ""
    reverseComplement = ""
    with open(filename, 'r') as f:
        for row in f:
            string = row.strip()
            if string[0] == '>':
                continue
            else:
                dnaString += string
                for x in string:
                    match x:
                        case 'A':
                            reverseComplement += 'T'
                        case 'T':
                            reverseComplement += 'A'
                        case 'C':
                            reverseComplement += 'G'
                        case 'G':
                            reverseComplement += 'C'

    reverseComplement = reverseComplement[::-1]

    logging.debug(dnaString)
    logging.debug(reverseComplement)

    candidate_protein_string = set()

    with concurrent.futures.ThreadPoolExecutor() as executor:
        future = executor.submit(template_function, dnaString)
        future2 = executor.submit(template_function, reverseComplement)
        result_list = future.result()
        logging.debug(result_list)
        result_list2 = future2.result()
        logging.debug(result_list2)
        candidate_protein_string = set(result_list+result_list2)


    with open(filename[:-4]+'_output.txt', 'w') as f:
        for x in candidate_protein_string:
            f.write(x+'\n')




