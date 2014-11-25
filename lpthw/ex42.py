
##Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
	pass

## ?? class Dog is-a Animal
class Dog(Animal):

	def __init__(self, name):
		## ?? class Dog has-a function that sets the name attribute (class Dog has-a name)
		self.name = name

## ?? class Cat is-a Animal
class Cat(Animal):

	def __init__(self, name):
		## ?? class Cat has-a function that sets the name attribute (class Cat has-a name)
		self.name = name

## ?? class Person is-a object
class Person(object):

	def __init__(self, name):
		## ?? class Person has a function that sets the name attribute (class Person has-a name)
		self.name = name

		##Person has-a pet of some kind
		self.pet = None

## ?? class Employee is-a Person
class Employee(Person):

	def __init__(self, name, salary):
		## ?? hmm what is this strange magic? class Employee has-a Parent that has-a function that sets the name attribute (class Employee has-a inherited name attribute)
		super(Employee, self).__init__(name)
		## ?? class Employee has-a salary attribute
		self.salary = salary

## ?? class Fish is-a object
class Fish(object):
	pass

## ?? class Salmon is-a Fish
class Salmon(Fish):
	pass

## ?? class Halibut is-a Fish
class Halibut(Fish):
	pass


## ?? instance rover is-a class Dog with name Rover
rover = Dog("Rover")

##?? instance satan is-a class Cat with name Satan
satan = Cat("Satan")

## ?? instance mary is-a person with name Mary
mary = Person("Mary")

## ?? instance mary has-a attribute pet equal to instance satan
mary.pet = satan

## ?? instance frank is-a Employee which inherits from (is-a) Person.  instance frank has name Frank, and salary 120000
frank = Employee("Frank", 120000)

## ?? instance frank has-a attribute pet equal to instance rover
frank.pet = rover

## ?? flipper is-a instance of class Fish
flipper = Fish()

## ?? crouse is-a instance of class Salmon which inherits from (is-a) class Fish
crouse = Salmon()

## ?? harry is-a instance of class Halibut which inherits from (is-a) class Halibut
harry = Halibut()