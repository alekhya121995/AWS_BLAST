import os
import sys



def getFSAFiles(directory):
    fsa_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".fsa"):
               #filenames = re.sub('.bai', '', os.path.join(root, file))
               filenames = file
               fsa_files.append(filenames)
    return(fsa_files)



fsafiles = getFSAFiles("/path/to/blast/files")

for i in range(len(fsafiles)):
    cmd = "sudo docker run --rm -v /opt/blast/blastdb:/opt/blast/blastdb:ro -v /opt/blast/blastdb:/blast/blastdb:ro  -v /opt/blast/queries:/blast/queries:ro -v /opt/blast/results:/blast/results:rw ncbi/blast blastn -task blastn-short -query /blast/queries/%s -db nt -taxids 9606 -out /blast/results/%s" % (fsafiles[i], fsafiles[i] )
    os.system(cmd)
    #print(cmd)
