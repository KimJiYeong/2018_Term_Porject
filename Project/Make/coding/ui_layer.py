from pico2d import *

class UI_wings:
    def __init__(self):
        self.image = load_image('resource\\UI.png')


        self.volume = load_music('The_Lapsed_Times.mp3')
        self.volume.set_volume(10)
        self.volume.play(1)


    def update(self):
        pass

    def draw(self):
        self.image.draw(1200 / 2, 1000 /2)
