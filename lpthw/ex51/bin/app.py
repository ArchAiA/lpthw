import web

urls = (
	'/hello', 'index', 
	'/foo', 'foo'
)

app = web.application(urls, globals())

render = web.template.render('templates/')

class index(object):
	def GET(self):
		greeting = "Hello World"
		return render.index(greeting = greeting)

class foo(object):
	def GET(self):
		foomessage = "This is the foo message"
		return render.foo(foomessage = foomessage)

if __name__ == "__main__":
	app.run()