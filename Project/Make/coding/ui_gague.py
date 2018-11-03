from pico2d import *

class UI_gague:
    def __init__(self):
        #size = 87 658
        self.image = load_image('Dream_gauge.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(87 + 950, 1000 - 658 + 100)
