from sys import argv

script, user_name, location = argv
prompt = 'fucking type an answer: '

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few quesetions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r.  Not sure where that is.
And you have a %r computer.  Nice.
""" % (likes, location, computer)