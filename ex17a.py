from sys import argv
from os.path import exists

#study drill #3: shortened the code as much as possible
script, from_file, to_file = argv
indata = open(from_file).read()
out_file = open(to_file, 'w').write(indata)
