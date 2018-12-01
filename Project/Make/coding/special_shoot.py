from pico2d import *
import game_world
import random
import player

count = None
class S_Shoot:
    image = None
    image2 = None
    def __init__(self, x = 400, y = 300, velocity = 1):
        if S_Shoot.image == None:
            S_Shoot.image = load_image('resource\\star2_21x21.png')
        if S_Shoot.image2 ==None:
            S_Shoot.image2 = load_image('resource\\star21x21.png')

        self.x, self.y, self.velocity = x, y, velocity
        self.count = random.randint(0, 1)

    def draw(self):
        if self.count % 2 == 0:
            self.image.clip_composite_draw(0, 0, 21, 21, self.y, ' ', self.x, self.y, 21 * 2, 21 * 2)
        else:
            self.image2.clip_composite_draw(0, 0, 21, 21, self.y, ' ', self.x, self.y, 21 * 2, 21 * 2)
        # 충돌체크
        draw_rectangle(*self.get_bb())

    def update(self):
        self.y += self.velocity
        if self.y < 25 or self.y > 1000 - 25:
            print('delete')
            game_world.remove_object(self)

    def get_bb(self):
        return self.x - 20, self.y - 20 , self.x + 20 , self.y + 20


