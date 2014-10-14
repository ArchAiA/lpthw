#argv is a function in sys that allows 
#command line parameters to be specified
from sys import argv

#assign the parameters in argv to variables
script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

#open the file specified through argv with the 'w' (write) argument for open
#assign the contents of the file specified in filename to target
print "Opening the file..."
#using open() with the 'w' argument automatically truncates the file...
#the other modes are r, and a.  a is for append.  r is for write.
#adding plus open the file in the mode in both read and write mode.

#SUMMARY OF OPEN ARGUMENTS
#'r' opens the file for reading with the pointer at the beginning of the file
#'r+' opens the file for reading and writing (updating) with the pointer at the beginning of the file
#'w' opens the file for writing, creates the file if it does not exist, and truncates the file
#'w+' opens the file for reading, and writing (updating), creates if it does not exist, and truncates
#'a' opens the file for appending with the pointer at the end of the file
#'a+' opens the file for appending, and reading (updating) with the pointer at the end of the file.
target = open(filename, 'a+')

#truncate deletes the contents of the file
print "Truncating the file.  Goodbye!"
#target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("Line 1: ")
line2 = raw_input("Line 2: ")
line3 = raw_input("Line 3: ")

#takes all of the raw input, and writes it to the file
#specified in target.
print "I'm going to write these to the file."

#target.write(line1)
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")

#study drill #3: Use strings, formats, and escapes to use one write line
#you must use %s 
#you must get your parentheses correct (remember this is a write function)
target.write("%s\n%s\n%s\n" % (line1, line2, line3))



#close saves the contents of target to the file
print "And finally, we close it"
target.close()