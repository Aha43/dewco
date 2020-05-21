from typing import List

from ...domain.util import list_to_str

class SenseDummy:
    """Fallback dummy api for the SenseHat API when nor a real Sense HAT system or emulator is avaliable"""

    def __init__(self):
        self.low_light = False

    #Environment
    def get_humidity(self):
        return 22.0
    def get_pressure(self):
        return 50.5
    def get_temperature(self):
        return 15.0
    def get_temperature_from_humidity(self):
        return 15.5
    def get_temperature_from_pressure(self):
        return 14.5

    #IMU

    #LED
    def set_rotation(self, r: int, redraw: bool = True) -> None:
        print("set_rotation: " + str(r))

    def flip_h(self, redraw: bool = True) -> None:
        print("flip_h: redraw: " + str(redraw))

    def flip_v(self, redraw: bool = True) -> None:
        print("flip_v: redraw: " + str(redraw))

    def set_pixel(self, x: int, y:int, r_or_rgb, g: int = None, b: int = None) -> None:
        if g == None and b == None:
            print("set_pixel: x: " + x + ", y: " + y +", rgb: " + list_to_str(r_or_rgb))
            self.rgb = r_or_rgb
        else:
            print("set_pixel: x: " + x + ", y: " + y +", r: " + r_or_rgb + ", g: " + g + ", b: " + b)
            self.rgb = [r_or_rgb, g, b]

    def get_pixel(self, x: int, y:int) -> List[int]:
        if self.rgb:
            return self.rgb
        self.rgb = [0, 0, 0]
        return self.rgb

    def load_image(self, file_path: str, redraw: True):
        print("load_image: file_path: " + file_path + ", redraw: " + str(redraw))

    def clear(self, color = [0, 0, 0]) -> None:
        print("clear: color: " + list_to_str(color))

    def show_message(self, text_string: str, scroll_speed: float, text_color = [255, 255, 255], back_color = [0, 0, 0]) -> None:
        print("show_message: text_string: " + text_string + ", text_color: " + list_to_str(text_color) + ", back_color: " + list_to_str(back_color))

    def show_letter(self, s: str, text_color = [255, 255, 255], back_color = [0, 0, 0]) -> None:
        print("show_letter: s: " + s + ", text_color: " + list_to_str(text_color) + ", back_color: " + list_to_str(back_color))

def SenseHat():
    return SenseDummy()
