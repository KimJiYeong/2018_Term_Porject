import random
import json
import os

from pico2d import *
import game_framework
import game_world

from player import Boy
from monster import Monster
from grass import Grass
from ui_layer import UI_wings
from ui_gague import UI_gague
from ui_heart import  UI_heart
from shoot import Shoot
name = "MainState"

boy = None
gauge = None
ball = None
def enter():
    global boy
    global gauge, ball
    boy = Boy()
    monster = Monster()
    grass = Grass()
    ui = UI_wings()
    gauge = UI_gague()
    heart = UI_heart()
    game_world.add_object(grass, 0)
    game_world.add_object(boy, 1)
    game_world.add_object(monster, 1)
    game_world.add_object(ui, 3)
    game_world.add_object(gauge, 4)
    game_world.add_object(heart, 4)


def exit():
    global boy, grass
    del boy
    del grass
    game_world.clear()


def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.quit()
        else:
            boy.handle_event(event)


def update():
    for game_object in game_world.all_objects():
        game_object.update()

def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()






