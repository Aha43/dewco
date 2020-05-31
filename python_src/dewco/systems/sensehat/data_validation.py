from typing import List

def check_sense_hat_led_pixel_coordinates(x: int, y: int):
    if x < 0:
        raise ValueError(f"x < 0 : {x}")
    if x > 7:
        raise ValueError(f"x > 7 : {x}")
    if y < 0:
        raise ValueError(f"y < 0 : {y}")
    if y > 7:
        raise ValueError(f"y > 7 : {y}")

def check_rgb_values(r: int, g: int, b: int):
    if r < 0:
        raise ValueError(f"r < 0 : {r}")
    if r > 255:
        raise ValueError(f"r > 255 : {r}")
    if g < 0:
        raise ValueError(f"g < 0 : {g}")
    if g > 255:
        raise ValueError(f"g > 255 : {g}")
    if b < 0:
        raise ValueError(f"b < 0 : {b}")
    if b > 255:
        raise ValueError(f"b > 255 : {b}")

def check_rgb_list(rgb: List[int]):
    if len(rgb) != 3:
        raise ValueError(f"rgb list length not 3 but {len(rgb)}")
    check_rgb_values(rgb[0], rgb[1], rgb[2])
