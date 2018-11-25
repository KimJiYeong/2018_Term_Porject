import game_framework
import title_state
from pico2d import *


name = "StartState"
image = None
logo_time = 0.0

def enter():
    global image
    image[0] = load_image('resource\\start_state_image\\num_0000.png')
    image[1] = load_image('resource\\start_state_image\\num_0001.png')
    image[2] = load_image('resource\\start_state_image\\num_0002.png')

    pass


def exit():
    global image
    del(image)
    pass


def update():
    global logo_time
    if(logo_time > 1.0):
        logo_time = 0
        #game_framework.quit()
        game_framework.change_state(title_state)
    delay(0.01)
    logo_time += 0.01

    pass


def draw():
    global image
    clear_canvas()
    for i in 3:
        image[i].draw(1200,1000)
    update_canvas()

    pass




def handle_events():
    events = get_events()
    pass


def pause(): pass


def resume(): pass




