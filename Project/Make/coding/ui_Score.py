from pico2d import *
import game_world
from monster_A import Monster
#애니메이션 프레임수
FRAMES_PER_ACTION = 6
#점수 출력

monster2 = None

class UI_score:
    def __init__(self):
        global monster2
        #size = 56 55
        self.score = 0
        self.pos_y = 1000 - 80
        self.pos_x = 1200 - 200

        self.font = load_font('ENCR10B.TTF' , 30) #폰트 업로드
    def update(self):
        pass

    def draw(self):
        self.font.draw(self.pos_x , self.pos_y ,'%d' %self.score , (93,91,160))
        pass
    def return_score(self):
        return self.score


