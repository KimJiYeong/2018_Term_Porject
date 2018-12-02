import game_framework
import main_state
from pico2d import *
import game_world
from ui_Score import UI_score
import title_state
name = "TutorialState"
image = None
tutorial_x , tutorial_y =1200 // 2 , 1000 //2

def enter():
    global image
    global title_bgm
    global tutorial_x , tutorial_y
    global score

    tutorial_x, tutorial_y = 1200 // 2, 1000 // 2
    image = load_image('resource\\ui\\tutorial.png')

    pass


def exit():
    global image
    global ms_x, mx_y
    global score

    del(image)
    ms_x = 0
    ms_y = 0

    score = 0
    pass


def handle_events():

    events = get_events()
    for event in events:
        if event.type == SDL_MOUSEBUTTONDOWN:
            game_framework.change_state(title_state)

    pass

def draw():
    clear_canvas()

    image.draw(1200 // 2, 1000 // 2)

    update_canvas()
    pass

def update():

    pass


def pause():
    pass


def resume():
    pass






