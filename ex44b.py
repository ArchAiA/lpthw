
class Other(object):

	def override(self):
		print "OTHER override()"

	def implicit(self):
		print "OTHER implicit()"

	def altered(self):
		print "OTHER altered()"


class Child(object):

	def __init__(self):
		self.other = Other() # self.other is a child of Other()

	def implicit(self):
		self.other.implicit() #this calls implicit in the Other class as other is a child of Other()

	def override(self):
		print "CHILD Override"

	def altered(self):
		print "CHILD BEFORE OTHER altered()" #this is a command in self.altered()
		print self.other.altered()			 #this is a command called from class Other()
		print "CHILD, AFTER OTHER altered()" #this is a command in self altered()


son = Child()


print "The first call to son.implicit results in a call to implicit in the parent method because"
print "son.other is set equal to a child of class Other() in the Child() init method"
print "essentially son.other = Other(), so calling son.implicit() is the same as calling"
print "Other.implicit()\n"
print "When son.override is called the method is run directly from the son instance of class Child\n"
print "When son.altered is called it is equivalent to calling Other.altered()\n"


son.implicit()
son.override()
son.altered()

print "\n\n\n Note that the only real difference betwen ex44b, and ex44a is that a Child.implicit() method had to be written."
print "This is because the Child() class does not inherit from a parent class that already contains the implicit method."