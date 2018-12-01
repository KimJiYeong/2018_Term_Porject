import game_framework
import title_state
from pico2d import *


name = "StartState"
#image = [[], [], []]
image = [None, None, None,
            None, None, None,
            None, None, None,
            None, None, None,
            None, None, None,
            None, None, None,
            None, None]
logo_time = 0.0

frame = 0

def enter():
    global image
    image[0] = load_image('resource\\start_state_image\\num_0000.png')
    image[1] = load_image('resource\\start_state_image\\num_0001.png')
    image[2] = load_image('resource\\start_state_image\\num_0002.png')
    image[3] = load_image('resource\\start_state_image\\num_0003.png')
    image[4] = load_image('resource\\start_state_image\\num_0004.png')
    image[5] = load_image('resource\\start_state_image\\num_0005.png')

    image[6] = load_image('resource\\start_state_image\\num_0006.png')
    image[7] = load_image('resource\\start_state_image\\num_0007.png')
    image[8] = load_image('resource\\start_state_image\\num_0008.png')

    image[9] = load_image('resource\\start_state_image\\num_0009.png')
    image[10] = load_image('resource\\start_state_image\\num_0010.png')
    image[11] = load_image('resource\\start_state_image\\num_0011.png')

    image[12] = load_image('resource\\start_state_image\\num_0012.png')
    image[13] = load_image('resource\\start_state_image\\num_0013.png')
    image[14] = load_image('resource\\start_state_image\\num_0014.png')

    image[15] = load_image('resource\\start_state_image\\num_0015.png')
    image[16] = load_image('resource\\start_state_image\\num_0016.png')
    image[17] = load_image('resource\\start_state_image\\num_0017.png')

    image[18] = load_image('resource\\start_state_image\\num_0018.png')
    image[19] = load_image('resource\\start_state_image\\num_0019.png')

    pass

def exit():
    global image
    del(image)
    pass


def update():
    global logo_time
    global frame
    if(logo_time > 19):
        logo_time = 0
        #game_framework.quit()
        game_framework.change_state(title_state)
    delay(0.01)
    logo_time += 0.05
    frame += 1

    pass


def draw():
    global image
    global logo_time
    clear_canvas()
    image[int(logo_time)].draw(1200 // 2,1000 // 2)
    update_canvas()

    pass




def handle_events():
    events = get_events()
    pass


def pause(): pass


def resume(): pass




