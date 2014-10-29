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
