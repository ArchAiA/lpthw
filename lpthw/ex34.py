animals = ["bear", "python", "peacock", "kangaroo", "whale", "platypus"]

print "The second animal at 1 is: ", animals[1]
print "The third animal at 2 is: ", animals[2]
print "The first animal at 0 is: ", animals[0]
print "The fourth animal at 3 is: ", animals[3]
print "The fifth animal at 4 is: ", animals[4]
print "The third animal at 2 is: ", animals[2]
print "The sixth animal at 5 is: ", animals[5]
print "The fifth animal at 4 is: ", animals[4]


#Using range(len) in a FOR loop for a list is useful because it shares mathematical properties with the ordinal number system
#Since lists count using ordinal numbers, the index value will be one less than the cardinal number
#Since range starts with 0 (when unspecified), and goes up to one before the end-number specified
# the whole "for i in range(len(animals)):" statement will start with zero and go up to 5, and will print all six elements. 
for i in range(len(animals)):
	print "Index %d in the list is %s." % (i, animals[i])

#If we just used "for i in animals:" i takes on the value of each element of animals
#Since the elements in animals are strings, i is not the index value in this case
#So we would have to do some extra programming to get the index value
for i in animals:
	print "Index %d in the list is %s." % (animals.index(i), i)

