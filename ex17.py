from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s." % (from_file, to_file)

#we can put the following two lines in one line of code, but this is not good form...
#in_file = open(from_file)
#indata = in_file.read()
indata = open(from_file).read()

print "The input file is %d bytes long" % len(indata)

print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, all done"


#closing the file does two things
# 1) it frees up resources 
# 2) it does not allow for any more changes to the file
#Python automatically closes a file when the reference object of a file is reassigned to another file. 
#It is a good practice to use the close() method to close a file.

out_file.close()

#indata.close() is not needed if we are going to combine the open, and read of from_file to indata
#indata.close()