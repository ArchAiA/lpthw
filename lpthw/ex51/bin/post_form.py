import web

# OMFG Why doesn't this fucking guy explain how any of this shit works?
urls = (
	'/hello', 'index', #This makes it so that localhost/hello points to the index.html file in the template directory
)

app = web.application(urls, globals())

render = web.template.render('templates/', base='layout')

class index(object):
	def GET(self): #GET tells the server to send a file back to the user's browser
		return render.hello_form() #render tells the server which file to render.  In this case, the hello_form

	def POST(self): #This takes the variables from hello_form() POSTs it to 'index' which is associated with '/hello'
		form = web.input(name="Nobody", greet="Hello")
		greeting = "%s %s" % (form.greet, form.name)
		return render.index(greeting = greeting)

if __name__ == "__main__":
	app.run()