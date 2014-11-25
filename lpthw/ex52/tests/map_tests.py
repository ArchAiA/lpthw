
from nose.tools import *
from gothonweb.map import *


# This tests the __init__ function of the Room() class.  
# The test creates a room, and then check to see
# if the room.name is equal to the parameter that test_room() sends 
# and tests if the room.paths dict is equal to an empty dict.
def test_room():
	gold = Room("GoldRoom", 
				"""This room has gold in it you can grab.  There's a door to 
				the north.""")
	assert_equal(gold.name, "GoldRoom")
	assert_equal(gold.paths, {})


# This tests the add_room() and go() methods of the Room() class.
# The test 1) creates instances of Room, 2) adds paths, 3) checks that the paths added are correct.
def test_room_paths():
	center = Room("Center", "Test room in the center.")
	north = Room("North", "Test room in the north.")
	south = Room("South", "Test room in the south.")

	center.add_paths({'north': north, 'south': south})
	assert_equal(center.go('north'), north)
	assert_equal(center.go('south'), south)


# This is an enflourishment of the previous test, and builds out an actual map
# and then tests the integrity of the map by making sure that the rooms make sense
# relative to each other.
#
# The test creates a 'west', and 'down' path from the 'start' room
# and then tests that the 'east' path from the 'west' room is the 'start' room.
def test_map():
	start = Room("Start", "You can go west and down a hole.")
	west = Room("Trees", "There are trees here, you can go east.")
	down = Room("Dungeon", "It's dark down here, you can go up.")

	start.add_paths({'west': west, 'down': down})
	west.add_paths({'east': start})
	down.add_paths({'up': start})

	assert_equal(start.go('west'), west)
	assert_equal(start.go('west').go('east'), start)
	assert_equal(start.go('down').go('up'), start)


def test_gothon_game_map():
	assert_equal(START.go('shoot!'), generic_death)
	assert_equal(START.go('dodge!'), generic_death)

	room = START.go('tell a joke')
	assert_equal(room, laser_weapon_armory)

	death = Room("death", "U R DAED")
	assert_equal(death.name, "death")
	assert_equal(death.description, "U R DAED")