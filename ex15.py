from sys import argv

#Takes the script name, and file name from argv.  
#The file name is taken from the first argument given by the user
script, filename = argv

#Opens the file name given by the user as an argument at the command line
txt = open(filename)

#Prints the name of the file
print "Here's your file %r:" % filename
#Prints the contents of the file
print txt.read()


#Get the file name via alternate means, by prompting the user
print "Type the file name again:"
file_again = raw_input(">")

#Opens the file that was specified at the prompt
txt_again = open(file_again)

#Prints the text from the file specified by the user
print txt_again.read()