
from sys import exit
#from random import randint
from ex_45_scenes import *
from ex45_engine import * #yes, yes, yes I know that import * is bad... just using it this time.
#from ex45_maps import Map








# a_map is an instance of class Map and is initialized with a_map.start_scene = 'gateway'
a_map = Map('gateway')

# a_game is an instance of class Engine and is initialized with a_game.scene_map = a_map
# ? Does this mean that a_game.scene_map is an instance of class Map ?
# ? More specifically, does this mean that a_game.scene_map is an instance of class Map initialized to a_game.scene_map = Map('gateway') ?
a_game = Engine(a_map)

# Run the play() method in a_game, which is an instance of Engine with method play()
a_game.play()