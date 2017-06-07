import tkengine

class View(object):

	def __init__(self, world, model):
		self.world = world
		self.window = world.window
		self.model = model
		self.player = model.player
		self.graphics = tkengine.TkGraphics("assets")
		self.player_sprite = self.graphics.load_sprite(
			"player.png", x=self.player.x, y=self.player.y, z=1)
		self.background_sprite = self.graphics.load_sprite(
			"background.png", x=0, y=0, z=0)

	def render(self):
		self.window.clear()
		self.background_sprite.x = self.player.x - 240
		self.player_sprite.y = self.player.y
		self.graphics.draw()