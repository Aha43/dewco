from typing import List

from ...domain.util import list_to_str

class SenseDummy:
    """Fallback dummy api for the SenseHat API when nor a real Sense HAT system or emulator is avaliable"""

    def __init__(self):
        self.low_light = False

        self.__led = [
            [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], 
            [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], 
            [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], 
            [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], 
            [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], 
            [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], 
            [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], 
            [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
        ]

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
        self.__check_led_pixel_coordinates(x, y)

        if g == None and b == None:
            self.__check_rgb(r_or_rgb[0], r_or_rgb[1], r_or_rgb[2])

            print("set_pixel: x: " + x + ", y: " + y +", rgb: " + list_to_str(r_or_rgb))

            self.__led[x][y][0] = r_or_rgb[0]
            self.__led[x][y][1] = r_or_rgb[1]
            self.__led[x][y][2] = r_or_rgb[2]

        else:
            self.__check_rgb(r_or_rgb, g, b)
            
            print("set_pixel: x: " + x + ", y: " + y +", r: " + r_or_rgb + ", g: " + g + ", b: " + b)
            
            self.__led[x][y][0] = r_or_rgb
            self.__led[x][y][1] = g
            self.__led[x][y][2] = b

    def get_pixel(self, x: int, y:int) -> List[int]:
        self.__check_led_pixel_coordinates(x, y)
        
        pixel = self.__led[x][y]
        return [pixel[0], pixel[1], pixel[2]]

    def load_image(self, file_path: str, redraw: True):
        print("load_image: file_path: " + file_path + ", redraw: " + str(redraw))

    def clear(self, color = [0, 0, 0]) -> None:
        print("clear: color: " + list_to_str(color))

        for i in range(7):
            for j in range(7):
                pixel = self.__led[i][j]
                for k in range(3):
                    pixel[k] = color[k]

    def show_message(self, text_string: str, scroll_speed: float, text_color = [255, 255, 255], back_color = [0, 0, 0]) -> None:
        print("show_message: text_string: " + text_string + ", text_color: " + list_to_str(text_color) + ", back_color: " + list_to_str(back_color))

    def show_letter(self, s: str, text_color = [255, 255, 255], back_color = [0, 0, 0]) -> None:
        print("show_letter: s: " + s + ", text_color: " + list_to_str(text_color) + ", back_color: " + list_to_str(back_color))

    def __check_led_pixel_coordinates(self, x: int, y: int):
        if x < 0:
            raise ValueError("x < 0")
        if x > 7:
            raise ValueError("x > 7")
        if y < 0:
            raise ValueError("y < 0")
        if y > 7:
            raise ValueError("y > 7")

    def __check_rgb(self, r: int, g: int, b: int):
        if r < 0:
            raise ValueError("r < 0")
        if r > 255:
            raise ValueError("r > 255")
        if g < 0:
            raise ValueError("g < 0")
        if g > 255:
            raise ValueError("g > 255")
        if b < 0:
            raise ValueError("b < 0")
        if b > 255:
            raise ValueError("b > 255")


def SenseHat():
    return SenseDummy()
