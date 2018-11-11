from pico2d import *

class Grass:
    def __init__(self):
        self.image = load_image('resource\\back_1.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(1200 / 2, 1000 /2)
