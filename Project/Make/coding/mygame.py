import game_framework
import pico2d

import main_state

pico2d.open_canvas(1200, 1000)
game_framework.run(start_state)
pico2d.close_canvas()