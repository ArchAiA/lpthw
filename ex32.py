the_count = [1, 2, 3, 4, 5]
fruits = ["apples", "oranges", "pears", "apricots"]
change = [1, "pennies", 2, "dimes", 3, "quarters"]

#This first kind of for-loop goes through a list

#a FOR loop for digits
for number in the_count:
	print "This is count: %d" % number

#A FOR loop for strings
for fruit in fruits:
	print "A fruit of type: %s." % fruit

#A FOR loop for mixed lists
for i in change:
	print "I got %r: " % i


#We can also use loops to build lists, first start with an empty one
elements = []
#Then use the range function to do 0 to 5 counts (explicitly finite iteration)
for i in range(0, 6): #range(x, y, z) where x equals start, y equals end, and z equals incrementor
	print "Adding %d to the list." % i
	elements.append(i) #Append is to add an item to the end of a list
	


#elements = range(0, 60) #We can just assign a list built from range() directly to the elements array as below


#Now we can print out the components of the elements list
for i in elements:
	print "Element was: %r" % i



#list functions
#list.append(x) - adds an item to the end of the list
#list.extend(L) - appends a list to the end of the list
#list.insert(i, x) - inserts variable x in position i
#list.remove(x) - removes the first value equal to x in the list.  If x is not in the list the function returns an error
#list.pop([i]) - returns, and removes the item at index position i.  If i is not specified, the last value in the list is popped
#list.index(x) - returns the index of the first value equal to x in the list.  If x is not in the list the function returns an error
#list.count(x) - counts the number of times that x appears in the list
#list.sort(cmp = None, key = None, reverse = False) - sorts a list according to the parameters.  See sort()
#list.reverse() - reverses the order of the list

#You can also make two dimensional lists like this: elements = [[1,2,3][a,b,c]]
#There is a difference between lists and arrays... We just don't know what yet
#The range function only includes numbers from the first to the last, but not including the last value