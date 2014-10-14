#Conver this while-loop to a function that you can call, and replace 6 in the test (i < 6) with a variable


def while_numbers(index, incrementor):
	i = 1
	numbers = []
	while i < index:
		print "At the top i is %d" % i
		numbers.append(i)

		i = i + incrementor
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i

	print numbers

	for num in numbers:
		print num

#To use this function you have to import the following in the calling code
# "from ex33a import while_numbers"

#Adding the second argument "incrementor" allows us to change how much the index is incremented at each iteration of the while loop



#Rewrite using FOR loop
def for_numbers(index, incrementor): #in the FOR loop the incrementor must be an integer...
	numbers = []
	for i in range(1, index, incrementor):
		print "At the top i is %d" % i
		numbers.append(i)
		#i = i + incrementor #This was added last.  It is unnecessary.  ? However the interesting thing is that this i, and the one evaluated in the loop are different? 
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i

	print numbers

	for num in numbers:
		print num
#We can see that with the FOR loop that the incrementation is done at the evaluation stage of the loop and that i is the same at the top and bottom
#of the code block because the iteration is done outside of the code block

