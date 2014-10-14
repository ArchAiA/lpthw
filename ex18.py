#components of a function
# 1) reserved word "def" declares that you are defining a function
# 2) the name that you give the function follows
# 3) in parentheses you list the arguments that are to be given to the function
# 4) a colon indicates that the function declaration is over, and that the function begins
# 5) any indented line following the colon indicates that the line is part of the function
# 6) the function ends with de-denting


#this one is like your scripts with argv
# *args indicates that all arguments passed to the function are to be contained in a list called args
def print_two(*args):
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" % (arg1, arg2)

#ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)

#this just takes one argument
def print_one(arg1):
	print "arg1: %r" % arg1

#this one takes no arguments
def print_none():
	print "I got nothin'."

print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()