import web
from bin.map import *

URL = (
	'/game', 'GameEngine',
	'/entry', 'Entry'
)

app = web.application(URL, locals())

if web.config.get('_session') is None:
	store = web.session.DiskStore('sessions')
	session = web.session.Session(app, store, initializer = {'room':None, 'name': 'Jedi'})
	web.config._session = session
else:
	session = web.config._session

render = web.template.render('templates/')




class Entry:
	def GET(self):
		return render.entry()
	def POST(self):
		form = web.input(name = "Jedi")
		if form.name != '':
			session.name = form.name
		session.room = map.START
		web.seeother("/game")


class GameEngine:
	def GET(self):
		if session.room:
			return render.show_room(room = session.room, name = sesion.name)
		else:
			return render.you_died()

	def POST(self):
		form = web.input(action=None)

		web.debug(session.room.name)
		if session.room and session.room.name != "The End" and form.action:
			session.room = session.room.go(form.action)

		web.seeother("/game")


if __name__ == "__main__":
	app.run()