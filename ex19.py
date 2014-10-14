#The variables in a function, and the arguments identified in a function definition are not connected
#unless they are explicitly passed


#this is the function definition.  It takes two arguments, and outputs them in strings
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket.\n"


#this is an example of calling the function with values
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)


#this is an example of calling the function using variables
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50
cheese_and_crackers(amount_of_cheese, amount_of_crackers)


#this is an example of calling a function using functions acting on values
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)


#this is an example of calling a function using functions acting on a combination of values and variables
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)