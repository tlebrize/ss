from pyglet.window import key

class Player(object):

	def __init__(self):
		self.x = 240
		self.dx = 100
		self.dy = 0
		self.y = 40

	def update(self, dt, keys):
		if keys[key.RIGHT]:
			self.x -= self.dx * dt
		if keys[key.LEFT]:
			self.x += self.dx * dt
		if keys[key.SPACE] and self.y == 40:
			self.dy = 210
		self.y += dt * self.dy
		if self.y < 40:
			self.dy = 0
			self.y = 40
		else:
			self.dy -= 16



class Model(object):

	def __init__(self, world):
		self.world = world
		self.player = Player()

	def update(self, dt, keys):
		self.player.update(dt, keys)