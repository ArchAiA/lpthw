import web

# OMFG Why doesn't this fucking guy explain how any of this shit works?
urls = (
	'/hello', 'index', #This makes it so that localhost/hello points to the index.html file in the template directory
)

app = web.application(urls, globals())

render = web.template.render('templates/')

class index(object):
	def GET(self):
		form = web.input(name="Nobody", greet=None) #Get input from web browser

		if form.greet:
			greeting = "%s, %s" % (form.greet, form.name)
			return render.index(greeting = greeting)
		else:
			return "Error: greet is required"

if __name__ == "__main__":
	app.run()