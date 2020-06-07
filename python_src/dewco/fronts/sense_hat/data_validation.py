from typing import List

def check_sense_hat_led_pixel_coordinates(x: int, y: int):
    if x < 0:
        #raise ValueError(f"x < 0 : {x}")
        raise ValueError("x < 0 : " + str(x))
    if x > 7:
        #raise ValueError(f"x > 7 : {x}")
        raise ValueError("x > 7 : " + str(x))
    if y < 0:
        #raise ValueError(f"y < 0 : {y}")
        raise ValueError("y < 0 : " + str(y))
    if y > 7:
        #raise ValueError(f"y > 7 : {y}")
        raise ValueError("y > 7 : " + str(y))

def check_rgb_values(r: int, g: int, b: int):
    if r < 0:
        #raise ValueError(f"r < 0 : {r}")
        raise ValueError("r < 0 : " + str(r))
    if r > 255:
        #raise ValueError(f"r > 255 : {r}")
        raise ValueError("r > 255 : " + str(r))
    if g < 0:
        #raise ValueError(f"g < 0 : {g}")
        raise ValueError("g < 0 : " + str(g))
    if g > 255:
        #raise ValueError(f"g > 255 : {g}")
        raise ValueError("g > 255 : " + str(g))
    if b < 0:
        #raise ValueError(f"b < 0 : {b}")
        raise ValueError("b < 0 : " + str(b))
    if b > 255:
        #raise ValueError(f"b > 255 : {b}")
        raise ValueError("b > 255 : " + str(b))

def check_rgb_list(rgb: List[int]):
    if len(rgb) != 3:
        #raise ValueError(f"rgb list length not 3 but {len(rgb)}")
        raise ValueError("rgb list length not 3 but " + str(len(rgb)))
    check_rgb_values(rgb[0], rgb[1], rgb[2])

def check_list_of_rgb(rgb_list: List[List[int]]):
    i = 0
    for rgb in rgb_list:
        if len(rgb) != 3:
            #raise ValueError(f"rgb list {i} length not 3 but {len(rgb)}")
            raise ValueError("rgb list " + str(i) + " length not 3 but " + str(len(rgb)))
        if rgb[0] < 0:
            #raise ValueError(f"r < 0 : {r} in list {i}")
            raise ValueError("r < 0 : " + str(rgb[0]) + " in list " + str(i))
        if rgb[0] > 255:
            #raise ValueError(f"r > 255 : {r} in list {i}")
            raise ValueError("r > 255 : " + str(rgb[0]) + " in list " + str(i))
        if rgb[1] < 0:
            #raise ValueError(f"g < 0 : {g} in list {i}")
            raise ValueError("g < 0 : " + str(rgb[1]) + " in list " + str(i))
        if rgb[1] > 255:
            #raise ValueError(f"g > 255 : {g} in list {i}")
            raise ValueError("g > 255 : " + str(rgb[1]) + " in list " + str(i))
        if rgb[2] < 0:
            #raise ValueError(f"b < 0 : {b} in list {i}")
            raise ValueError("b < 0 : " + str(rgb[2]) + " in list " + str(i))
        if rgb[2] > 255:
            #raise ValueError(f"b > 255 : {b} in list {i}")
            raise ValueError("b > 255 : " + str(rgb[2]) + " in list " + str(i))
        i = i + 1
