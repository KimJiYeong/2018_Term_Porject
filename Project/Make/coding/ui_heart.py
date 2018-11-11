from pico2d import *
#애니메이션 프레임수
FRAMES_PER_ACTION = 6

class UI_heart:
    def __init__(self):
        #size = 56 55
        self.image_heart1 = load_image('resource\\heart.png')
        self.image_heart2 = load_image('resource\\heart.png')
        self.image_heart3 = load_image('resource\\heart.png')
        self.button_y = 100

    def update(self):
        pass

    def draw(self):
        self.image_heart1.draw(56 * 1 + 5, 1000 - 80)
        self.image_heart2.draw(56 * 2 + 10, 1000 - 80)
        self.image_heart3.draw(56 * 3 + 15, 1000 - 80)