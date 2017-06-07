import pyglet, os

class Animation(object):
	def __init__(self, image, size, batch, x=0, y=0):
		self.image = image
		self.sequence = pyglet.image.ImageGrid(image, *size)
		self.sprite = pyglet.sprite.Sprite(self.sequence[0], x=x, y=y,
			batch=batch)

	def swicth(self, num):
		self.sprite.image = self.sequence[num]

class TkGraphics(object):

	def __init__(self, sources):
		self.images = {}
		self.sprites = []
		self.sequences = []
		self.batches = [pyglet.graphics.Batch() for _ in range(256)]
		for file in os.listdir(sources):
			self.images.update({file: pyglet.image.load(sources + "/" + file)})

	def load_sprite(self, name, x=0, y=0, z=0, color=None, scale=None):
		z = max(min(z, 255), 0)
		sprite = pyglet.sprite.Sprite(self.images.get(name), x=x, y=y,
			batch=self.batches[z])
		if color:
			sprite.color = color
		if scale:
			sprite.scale = scale
		self.sprites.append(sprite)
		return sprite

	def load_animation(self, name, size, x=0, y=0, z=0, color=None, scale=None):
		z = max(min(z, 255), 0)
		animation = Animation(self.images.get(name), size, self.batches[z], x=0, y=0)
		self.sprites.append(animation.sprite)
		return animation

	def draw(self):
		for batch in self.batches:
			batch.draw()

class View(object):

	def __init__(self, world, model):
		self.world = world
		self.window = world.window
		self.model = model
		self.player = model.player
		self.graphics = TkGraphics("assets")
		self.player_animation = self.graphics.load_animation("player_all.png", 
			(1, 4), x=self.player.x, y=self.player.y, z=1)
		self.background_sprite = self.graphics.load_sprite(
			"background.png", x=0, y=0, z=0)

	def render(self):
		self.window.clear()
		self.background_sprite.x = self.player.x - 240
		self.player_animation.sprite.y = self.player.y
		self.graphics.draw()