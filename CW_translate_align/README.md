# This is a simple tool written in Python3 to translate and align two nucleotide sequences. Specifically used here to compare the similarity of nanobodies with the same target protein. However this could be altered to align and compare any two proteins.
#
# To run:
# 1. Download all scripts and the sample data set in this repository. Ensure these are in the same directory.
# 2. Ensure the modules 'Pandas' and 'BioPython' are installed and available
# 3. Run the translatealign.py script. At several points in this script user input will be requested; follow instructions in bold red carefully.
# 
# The sequence will product a number of pairwise alignments generated through pairwise2. Comparison is achieved visually, '|' between amino-acid residues represents complete conservation; '.' represents conservation of chemical properties between residues. When using the example dataset, strong conservation is expected at both the N-terminus and C-terminus due to the presence of highly conserved expression and purification sequences.
# 
# 4. Utilisation of a different set of sequences is possible, however this will require minor edits to the code on lines 11 & 12 to ensure the file is read in correctly. Also files must be of the .csv filetype and formatted in a similar way to the sample data set
# 5. If running in python, the command 'run translatealign.py' will start the script. If running from the windows command line use 'python translatealign.py'.
#
# This script is best run using a python console, as this will improve usability. It is still viable to run through the windows command line
