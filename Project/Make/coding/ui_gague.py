from pico2d import *

class UI_gague:
    def __init__(self):
        #size = 87 658
        self.image_gauge = load_image('Dream_gauge.png')
        self.image_button = load_image('Dream_Button.png')
        self.button_y = 100

    def update(self):
        self.button_y = (self.button_y + 2)
        self.button_y = clamp(100  , self.button_y , 658)
        pass

    def draw(self):
        self.image_gauge.draw(87 + 950, 1000 - 658 + 100)
        self.image_button.draw(87 + 950, self.button_y)
