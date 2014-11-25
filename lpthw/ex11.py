print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh",

#Notice the prompt argument in this last raw_input() function
weight = raw_input(":")
print "How much money do you have",

#Notice the prompt argument in this last raw_input() function
#Also notice the escape character which eliminates the space before
#the prompt, and the space after the colon
money = raw_input("\b: ")

#Notice in the output for the height variable 
print "So, you're %r old, %r tall, and %r heavy." % (age, height, weight)