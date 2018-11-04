
# layer 0: Background Objects
# layer 1: Foreground Objects
# layer 2: Shooting star
# layer 3: UI Objects
# layer 4: UI_sub Objects

objects = [[], [], [], [], []]



def remove_object(o):
    print("delete")
    for i in range(len(objects)):
        if o in objects[i]:
            objects[i].remove(o)
            del o
            return


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
