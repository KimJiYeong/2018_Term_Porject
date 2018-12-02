from pico2d import *

class UI_wings:
    def __init__(self):
        self.image = load_image('resource\\ui\\UI.png')



    def update(self):

        pass

    def draw(self):
        self.image.draw(1200 / 2, 1000 /2)
