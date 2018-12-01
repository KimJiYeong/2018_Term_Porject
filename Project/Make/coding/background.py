from pico2d import *
import game_framework

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1 / TIME_PER_ACTION
#애니메이션 프레임수
FRAMES_PER_ACTION = 20

class Background:
    def __init__(self):
        self.image = load_image('resource\\scroll_map_01.png')
        self.scroll_y = 1000
    def update(self):
        self.scroll_y = clamp(1000 // 2 , FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time + self.scroll_y, 5000 - 1000)
        pass

    def draw(self):
        self.image.clip_draw(0, int(self.scroll_y), 1200, 1000, 1200// 2 , 1000 // 2)
