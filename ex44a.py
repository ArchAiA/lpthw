

#Note how son which is a class of type Parent inherits the implicit() function from Parent
class Parent(object):

	def implicit(self):

		print "PARENT implicit()"

class Child(Parent):
	pass

dad = Parent()
son = Child()


print "class Child is a class of type Parent"
print "son, an instance of class Child, inherits the implicit() method from class Parent"
print "so calling son.implicit() results in the same output as calling dad.implicit()"
print "All methods defined in a base class are present in all subclasses"
print "The actual output from the program is below:\n"
dad.implicit()
son.implicit()
print "\n\n\n"




#Overriding Explicitly
#If you define a method with the same name in a child class as exists in a parent class
#The the child class method will be run instead of the parent class method


class Parent(object):

	def override(self):
		print "PARENT Override"

class Child(Parent):

	def override(self):
		print "CHILD Override"

dad = Parent()
son = Child()


print "Since the child method, and the parent method both contain methods with the same name."
print "When the child version of the method is called it will no longer inherit the parent method."
print "The child method will be run instead.\n"

dad.override()
son.override()

print "\n\n\n"




#Even when a parent method is overridden, you can call the original parent method using super

class Parent(object):
	def altered(self):
		print "PARENT Altered()"

class Child(Parent):
	def altered(self):
		print "CHILD, BEFORE PARENT altered()"
		super(Child, self).altered() #Note, this means you are calling the parent of the Child class, and passing self
		print "CHILD, AFTER PARENT altered()"

dad = Parent()
son = Child()

print "In this case the original parent version of the method is run first"
print "Next the child method overrides the parent method"
print "And then the original parent method is called from within the child method using super()"
dad.altered()
son.altered()