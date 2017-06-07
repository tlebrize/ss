import tkengine, pyglet

class Controller(tkengine.TkScene):
	def __init__(self, world, model, view):
		super(Controller, self).__init__(world)
		self.model = model
		self.view = view
		self.key_handlers = {
			pyglet.window.key.ESCAPE	: pyglet.app.exit,
		}
		pyglet.clock.schedule_interval(self.update, 1/120)

	def update(self, dt):
		self.model.update(dt, self.keys)
		self.view.render()
