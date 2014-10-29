class Engine(object):

	def __init__(self, scene_map):
		self.scene_map = scene_map

	def play(self):
		current_scene = self.scene_map.opening_scene()

		while True:
			print "___________________________________________"
			
			# This takes the return value from enter() and sets next_scene equal to it.
			next_scene_name = current_scene.enter()
			# This then sets current_scene equal to the DICT value associated with the key.  The key in this case is the value returned from the enter() in the above line.
			current_scene = self.scene_map.next_scene(next_scene_name)
			


