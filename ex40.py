#Class definition for class Song
class Song(object):
	def __init__(self, lyrics): #The def __init__() function automatically runs at instantiation
		self.lyrics = lyrics #I'm guessing that every init function has 'self' as the first argument by default, and 'self' does not need to have anything passed to it.

	def sing_me_a_song(self): #So calling self.sing_me_a_song actually calls sing_me_a_song(self).  It is the method-way of calling a function
		for line in self.lyrics:
			print line






#Instantiation of class Song.  
#The argument is a list that get assigned to lyrics under the def __init__(self, lyrics) part of the class definition
#In the statement self.lyrics = lyrics  
happy_bday = Song(["Happy birthday to you",
					"I don\'t want to get sued",
					"So I\'ll stop right there"])

#Instantiaion of class Song
bulls_on_parade = Song(["They rally around the family",
						"With pockets full of shells"])


#Instantiation of class Song
sail = Song(["This is how I show my love", "I made it in my mind because",
			"I blame it on my ADD baby."])


test_lyrics = ["Remember when my first meal was school lunch", "Now I spit a fifteen straight with no punch"]
grown_up = Song(test_lyrics)


#Calling methods using methods in instantiations that were inherited from class Song
happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()
sail.sing_me_a_song()
grown_up.sing_me_a_song()

#You can also print the object attribute/property "lyrics" which returns the list given as an argument at instantiation
print sail.lyrics
print grown_up.lyrics