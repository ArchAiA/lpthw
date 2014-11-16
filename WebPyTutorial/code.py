# THIS IS THE FIRST EXAMPLE IN THE WEB.PY TUTORIAL
# AND IS ABOUT BASIC MECHANICS


import web #Imports the web.py module



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
		return "Hello World"

class About:
	def GET(self):
		return "We are a bla bla bla company that does bla bla bla"


if __name__ == "__main__":
	app.run()