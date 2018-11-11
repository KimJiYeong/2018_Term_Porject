
# layer 0: Background Objects
# layer 1: Foreground Objects
# layer 2: Shooting star : Player
# layer 3: Shooting star : Monster
# layer 4: UI Objects
# layer 5: UI_sub Objects

objects = [[], [], [], [], [], []]



def remove_object(o):
    print("delete")
    for i in range(len(objects)):
        if o in objects[i]:
            objects[i].remove(o)
            del o
            break


def check_object(layer):
    for i in objects[layer]:
        yield i

def clear():
    for o in all_objects():
        del o
    objects.clear()


def all_objects():
    for i in range(len(objects)):
        for o in objects[i]:
            yield o

def add_object(o, layer):
    objects[layer].append(o)

#충돌체크
def collide(a,b):
    left_a , bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True
