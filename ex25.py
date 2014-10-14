def break_words(stuff):
	"""This function will break up words for us."""
	words = stuff.split(' ')
	return words

def sort_words(words):
	"""Sorts the words."""
	return sorted(words)

def print_first_word(words):
	"""Prints the first word after popping it off."""
	word = words.pop(0)
	print word

def print_last_word(words):
	"""Prints the last word after popping it off."""
	word = words.pop(-1)
	print word

def sort_sentence(sentence):
	"""Takes in a full sentence ard returns the words after sorting."""
	words = break_words(sentence)
	return sort_words(words)

def print_first_and_last(sentence):
	"""Prints the first and last words of the sentence."""
	"""This takes sentence, breaks it up, places the individual words in a list, and then prints the first and last ones"""
	words = break_words(sentence)
	print_first_word(words)
	print_last_word(words)

def print_first_and_last_sorted(sentence):
	"""Sorts the words in a sentence and then prints the first and last one."""
	words = sort_sentence(sentence)
	print_first_word(words)
	print_last_word(words)
