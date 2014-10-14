#argv is a function in sys that allows 
#command line parameters to be specified
from sys import argv

script, filename = argv
target = open(filename)

#print the output of the function read()
print target.read()

target.close()