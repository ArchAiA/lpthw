

import random
from urllib import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []


#This creates a dict that appears to have object instantiations as the keys, and explanations as the values
PHRASES = {
	"class %%%(%%%):":
	 "Make a class named %%% that is-a %%%.",
	"class %%%(object):\n\tdef __init__(self, ***)" :
	 "class %%% has-a __init__ that takes self and *** parameters.",
	"class %%%(object):\n\tdef ***(self, @@@)":
	 "class %%% has-a function named *** that takes self and @@@ paramters.",
	"*** = %%%()":
	 "From *** get the *** function, and call it with parameters self, @@@.",
	"***.*** = '***'":
	 "From *** get the *** attribute and set it to '***'."
}



#Do they want to drill phrases first
#If two arguments are used at the command line, and the second arg is english set PHRASE_FIRST to True
PHRASE_FIRST = False
if len(sys.argv) == 2 and sys.argv[1] == "english":
	PHRASE_FIRST = True


#Load up the words from the website
for word in urlopen(WORD_URL).readlines(): #Takes words from text file in website, and reads them (WORD_URL set in LINE 7)
	WORDS.append(word.strip()) #For every word at the specified web page append to the WORDS list and strip whitespace


def convert(snippet, phrase):
	class_names = [w.capitalize() for w in #Capitalize all of the words in a random sample of the WORDS list
					random.sample(WORDS, snippet.count("%%%"))] #Return X words from the WORDS list where x is # of times that %%% shows up in snippet
	other_names = random.sample(WORDS, snippet.count("***")) #Return X words from the WORDS list where x is the # of times that *** shows up in snippet.  Assign to list? other_names?

	results = [] #Create a list called results
	param_names = [] #Create a list called param_names

	for i in range(0, snippet.count("@@@")): #Do this loop the number of times that @@@ shows up in the snippet
		param_count = random.randint(1, 3) #Create a list of randomly generated numbers and store in param count
		param_names.append(', '.join(random.sample(WORDS, param_count))) #Append to list param_names a set of joined words.  The number of words to be joined was determined in the line above by random number generation

	for sentence in snippet, phrase: #Loop through snippet, and phrase each.
		result = sentence[:] #Set result equal to all of the contents of the sentence list during each loop iteration

		#Fake class names
		for word in class_names: #For each item in list class_names
			result = result.replace("%%%", word, 1) #replace each %%% in the string result with a word in class_names list.  Do this only once for each loop iteration.

		#Fake other names
		for word in other_names: #For each item in list other_names
			result = result.replace("***", word, 1) #Replace each *** in the string with a word from the other_names list.  Do this only once for each loop iteration.

		#Fake parameter lists
		for word in param_names: #For each item in list param_names
			result = result.replace("@@@", word, 1) #Replace each @@@ with a word from the param_names list.  Do this only once per loop iteration.

		results.append(result) #Append result to teh results list

	return results





#Keep going until they hit CTRL-D
try:
	while True:
		snippets = PHRASES.keys() #Create a list of the keys in phrases and assign to snippets
		random.shuffle(snippets) #Shuffle the items in list snippets in place

		for snippet in snippets: #For each item in list snippets
			phrase = PHRASES[snippet] #Create a list called phrase, and assign each value in PHRASES that is associated with snippet (remember) snippets is a list of keys, to phrase.
			question, answer = convert(snippet, phrase) #Call the convert method using the randomly shuffled, then chosen key, and the value associated with that key, and assign the return results to question, and answer
			if PHRASE_FIRST: #If PHRASE_FIRST is True (meaning "english" was spcified)
				question, answer = answer, question #Set question to answer, and answer to question?

			print question

			raw_input("> ")
			print "ANSWER: %s\n\n" % answer

except EOFError:
	print "\nBye"






#Blank Spot Exercise (Page 145)
#class ???(Y)
#class ???(Y): def __init__(self, ???)
#class ???(Y): def ???(self, ???)
#foo = ???()
#foo.???(???, ???)
#foo.??? = ???