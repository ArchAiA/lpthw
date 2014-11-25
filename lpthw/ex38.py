ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there's not 10 things in that list, let's fix that."

stuff = ten_things.split(" ") #SD01: split(ten_things, " ")
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
	next_one = more_stuff.pop() #SD01: pop(next_one, more_stuff)
	print "Adding: ", next_one
	stuff.append(next_one) #SD01: append(stuff, next_one)
	print "There's %d items now." % len(stuff)

print "There we go: ", stuff

print "Let's do some things with stuff."

print stuff[1]
print stuff[-1]
print stuff.pop() #SD01: pop(stuff)
print ' '.join(stuff) #SD01: join(' ', stuff)
print '#'.join(stuff[3:5]) #SD01: join(' ', stuff[3:5])