from random import randint #Why can't this just be in the import section of the ex45_main.py file?

class Scene(object):

	def enter(self):
		exit(1)


class Death(Scene):

	quips = ["You died.  You suck at life.",
			"Here's your one day chip from Awesome Anonymous.  Congratulations for not being awesome."
			"Beter the greatest failure than a mediocre success...  Unless of course you, are you... which you are."
			"You are dead.  That is all."
	]

	def enter(self):
		print Death.quips[randint(0, len(self.quips)-1)]
		exit(1)


class Gateway(Scene):

	def enter(self):
		print "You are standing in a foyer.  There are rats in the front room, roaches in the back,"
		print "and a junkie in the alley with a baseball bat.\n"
		print "Do you:"
		print "\tGo into the [front] room."
		print "\tGo into the [back] room."
		print "\tGo into the [alley]."
		print "\tTry to [run] away."

		action = raw_input(">")

		if action == "front":
			print "You were eaten by a giant rat."
			return 'death'

		elif action == "back":
			print "You were eaten by a pack of roaches."
			return 'death'

		elif action == "run":
			print "Real gangsta-ass n****z don't run from shit, cuz real gangsta-ass n****z can't run fast."
			return 'death'

		elif action == "alley":
			print "You walk into the alleyway, and encounter a junkie.  The junkie hands you a bottle of old petroleum, and walks away."
			return 'alleyway'

		else:
			print "I don't understand."
			return 'gateway'


class Alleyway(Scene):

	def enter(self):
		print "After the junkie leaves the alleyway you look around and all you see are broken shards of glass and needles."
		print "Do you:"
		print "\tPick up a [needle]."
		print "\tPick up a shard of [glass]."

		action = raw_input(">")

		if action == "needle":
			print "You prick yourself by accident and die 20 years later."
			return 'death'

		elif action == "glass":
			print "You cut yourself by accident and die 20 years later."
			return 'death'

		else:
			print "I'm sorry, I don't understand."
			return 'alleyway'


class Map(object):

	scenes = {
		'gateway': Gateway(),
		'alleyway': Alleyway(),
		'death' : Death()
	}


	def __init__(self, start_scene):
		self.start_scene = start_scene


	# This takes the argument, then uses it as a key to return a value from a DICT
	def next_scene(self, scene_name):
		return Map.scenes.get(scene_name)


	# All this does is run next_scene() while passing self.start_scene as an argument...  Why is this needed?
	def opening_scene(self):
		return self.next_scene(self.start_scene)
