from pico2d import *
import game_world

class Shoot:
    image = None

    def __init__(self, x = 400, y = 300, velocity = 1):
        if Shoot.image == None:
            Shoot.image = load_image('resource\\monster\\monster_shoot.png')
        self.x, self.y, self.velocity = x, y, velocity

    def draw(self):
        self.image.draw(self.x, self.y)

        # 충돌체크
        #draw_rectangle(*self.get_bb())

    def update(self):
        self.y += self.velocity

        if self.y < 25 or self.y > 1000 - 25:
            print('delete')
            game_world.remove_object(self)

    def get_bb(self):
        return self.x - 10, self.y - 10 , self.x + 10 , self.y + 10


