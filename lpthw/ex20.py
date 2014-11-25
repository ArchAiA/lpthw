
from sys import argv

script, input_file = argv

def print_all(f):
	print f.read()

def rewind(f):
	#seek moves the point to a location, and is used as seek(offset, from_what).
	#the from_what argument is 0 for beginning of file (default), 1 for current position, and 2 for end of file
	f.seek(0) 


def print_a_line(line_count, f):
	print line_count, f.readline()

current_file = open(input_file)

print "First let's print the whole file:\n",

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

#current_line = current_line + 1
#use increment instead
current_line += 1
print_a_line(current_line, current_file)

#current_line = current_line + 1
#use increment instead
current_line += 1
print_a_line(current_line, current_file)