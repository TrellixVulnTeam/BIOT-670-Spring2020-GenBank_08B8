
import os
from Bio import SeqIO
from Bio import Entrez
import CircularView
import LinearView
def Main():  
    val = input("Enter your accession: ") 
    print(val)
    val2 = input("Enter your email: ")
    GB_Hunter(val,val2)
    CircularView.rec_it(open("working.gb"))



def GB_Hunter (accession, email):
    Entrez.email = email  # Always tell NCBI who you are
    filename = accession + ".gb"
    if not os.path.isfile(filename):
        # Downloading...
        net_handle = Entrez.efetch(
            db="nucleotide", id=accession, rettype="gb", retmode="text"
        )
        out_handle = open(filename, "w+")
        out_handle.write(net_handle.read())
        out_handle.close()
        net_handle.close()
        print("Saved")

    print("Parsing...")
    record = SeqIO.read(filename, "genbank")
    SeqIO.write(record,"working.gb","genbank")
    print(record)
    return
Main()