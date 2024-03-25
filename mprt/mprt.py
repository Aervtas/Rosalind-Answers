import logging
import sys, re, requests

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
# logging.disable(logging.CRITICAL)

filename = sys.argv[1]

n_glycosylation_motif = re.compile('N[^P][ST][^P]')

with open(filename, 'r') as f:
    for row in f:
        accessID = row.strip()
        accessQuery = accessID.split('_')[0]
        try:
            r = requests.get('https://rest.uniprot.org/uniprotkb/'+accessQuery+'.fasta')
        except requests.exceptions.RequestException as e:
            logging.error("Access ID: "+accessID+"  failed with error "+str(e))

        protData = r.text
        protData = protData.split('\n')
        protData = ''.join(protData[1:])
        indices = []
        for i in range(0, len(protData) - 4):
            if n_glycosylation_motif.match(protData[i: i+4]):
                indices += [str(i+1)]

        if indices != []:
            with open(filename[:-4]+"_output.txt", 'a') as outfile:
                outfile.write(accessID+"\n"+ ' '.join(indices) +"\n")