import tkengine
from resources.model import Model
from resources.view import View
from resources.controller import Controller

def main():
	window = tkengine.TkWindow(480, 340)
	world = tkengine.TkWorld(window)
	model = Model(world)
	view = View(world, model)
	controller = Controller(world, model, view)
	world.add_scenes({"controller": controller})
	world.run("controller")

if __name__ == "__main__":
	main()