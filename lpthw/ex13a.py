from sys import argv

script, first, second  = argv
age = raw_input("What is your age: ")

print "Your script is called: %r \nYour first variable is %r \nYour second variable is %r \nYou are %r years old" % (script, first, second, age)