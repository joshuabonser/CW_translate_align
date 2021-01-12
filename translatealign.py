####Input box title formatting####

class colour:
   RED = '\033[91m'
   BOLD = '\033[1m'
   END = '\033[0m'

####importing the .csv file containing the DNA sequences####

import pandas as pd #pandas required for read_csv command as data formatted in excel
nanobody_seqs = "nanobody_seqs.csv" #data could not pull the file from the local environment, thus an object had to be created
seqs = pd.read_csv(nanobody_seqs)
seq_dict = dict(seqs.values.tolist()) #data could no be pulled effectively from the table itself, dictionary created to ease this
for key, value in seq_dict.items():
    print(key, ':', value)  #originally print layout of the dictionary was cumbersome and hard to read, print over multiple lines due to necessity for the next step
print("")

####translation of the first chosen sequence####

print(colour.RED + colour.BOLD + "Input first sequence identifier from above dictionary (e.g. KuCC_syn5)" + colour.END)
NB = seq_dict[input()]
UNB = NB.upper() #dictionary in the function required uppercase nucleotide sequence, addition of .upper converts the lowercase sequences to uppercase
print(UNB) #NB and UNB are temporary objects for converting the string to be usable in the Translate function
import translate #to make to code more reusable for a second translation, the translation function was added to a module
TNB = translate.translate(UNB) #TNB is a temporary object for addition to the translated sequence dictionary
print("")
print(colour.RED + colour.BOLD + "Translated sequence:" + colour.END)
print(TNB)
print("")
print(colour.RED + colour.BOLD + "Assign a name to the translated sequence" + colour.END)
translated = dict()
translated.update({input(): TNB})
print(translated)

####translation of the second chosen sequence####

for key, value in seq_dict.items():
    print(key, ':', value)
print("")
print(colour.RED + colour.BOLD + "Input second sequence identifier from above dictionary (e.g. KuCC_syn5)" + colour.END)
NB = seq_dict[input()]
UNB = NB.upper() #dictionary in the translate function required uppercase nucleotide sequence, addition of .upper converts the lowercase sequences to uppercase
print(UNB) #NB and UNB are temporary objects for converting the string to be usable in the Translate function
import translate
TNB = translate.translate(UNB) #TNB is a temporary object for addition to the translated sequence dictionary
print("")
print(colour.RED + colour.BOLD + "Translated sequence:" + colour.END)
print(TNB)
print("")
print(colour.RED + colour.BOLD + "Assign a name to the translated sequence" + colour.END)
translated.update({input():TNB})
print("")
print("")
print(colour.RED + colour.BOLD + "Translations chosen are shown below" + colour.END) #for confirmation of successful translation the dictionary is printed again
print("")
for key, value in translated.items():
    print(key, ':', value)
    
####Pairwise sequence alignment of the two chosen sequences####
from Bio import pairwise2
#The Biopython package contains modules for aligning sequences, as well as visualising the alignment.  Thus they were used here
from Bio.Seq import Seq
#Seq is imported to allow pairwise2 to read the inputs as sequences
from Bio.pairwise2 import format_alignment
#format_alignment will allow visual representation of the pairwise sequence alignment
print("")
print(colour.RED + colour.BOLD + "Input first assigned sequence name" + colour.END)
seq1 = Seq(translated[input()])
print("")
print(colour.RED + colour.BOLD + "Input second assigned sequence name" + colour.END)
seq2 = Seq(translated[input()])
print("")
print("")
alignments = pairwise2.align.localxx(seq1, seq2)
for alignment in alignments: 
    print(format_alignment(*alignment))
print("")
print(colour.RED + colour.BOLD + "Local alingments are presented above. Decrease in zoom may be required to view accurately on a single line" + colour.END)