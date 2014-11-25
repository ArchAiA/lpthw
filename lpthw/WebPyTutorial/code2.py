# THIS IS EXAMPLE 2 IN THE WEB.PY TUTORIAL
# THIS EXAMPLE COVERS TEMPLATING
# AND MAKES USE OF THE templates DIRECTORY

import web #Imports the web.py module

render = web.template.render('templates/') #This tells web.py where the templates are located

# Tells web.py what our how the URLs are structured
# This says that we want the / URL to be handled by the class named Index
# The line after says that the /about URL should be handled by the class named About
urls = (
	'/', 'Index',
	'/about', 'About'

)

app = web.application(urls, globals())


class Index:
	def GET(self): # This GET function will now run any time a user requests the / URL
#		return "Hello World" CHANGED FROM VERSION 1 FOR TEMPLATING TUTORIAL
		name = 'Bob'
		return render.index(name) # index is the name of the template, and name is the argument passed to it

class About:
	def GET(self):
		return "We are a bla bla bla company that does bla bla bla"


if __name__ == "__main__":
	app.run()