from typing import List

from .color_map import color_map_builder
from .data_validation import (check_rgb_list, check_rgb_values,
                              check_sense_hat_led_pixel_coordinates)


class SenseDummy:
    """Fallback dummy api for the SenseHat API when nor a real Sense HAT system or emulator is avaliable"""

    def __init__(self):
        self.low_light = False

        self.__led_matrix = [
            [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [
                0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
            [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [
                0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
            [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [
                0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
            [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [
                0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
            [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [
                0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
            [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [
                0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
            [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [
                0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
            [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [
                0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
        ]

    # Environment
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

    # IMU

        # TODO :D

    # LED
    def set_rotation(self, r: int, redraw: bool = True) -> None:
        print("set_rotation: " + str(r))

    def flip_h(self, redraw: bool = True) -> None:
        print("flip_h: redraw: " + str(redraw))

    def flip_v(self, redraw: bool = True) -> None:
        print("flip_v: redraw: " + str(redraw))

    def set_pixels(self, pixels: List[List[int]]) -> None:
        builder = color_map_builder()
        builder.append_pixels(pixels)
        cm = builder.build()
        self.__led_matrix = cm.get_matrix()

    def set_pixel(self, x: int, y: int, r_or_rgb, g: int = None, b: int = None) -> None:
        check_sense_hat_led_pixel_coordinates(x, y)

        if g == None and b == None:
            check_rgb_list(r_or_rgb)

            print("set_pixel: x: " + x + ", y: " +
                  y + ", rgb: " + str(r_or_rgb))

            self.__led_matrix[x][y][0] = r_or_rgb[0]
            self.__led_matrix[x][y][1] = r_or_rgb[1]
            self.__led_matrix[x][y][2] = r_or_rgb[2]

        else:
            check_rgb_values(r_or_rgb, g, b)

            print("set_pixel: x: " + x + ", y: " + y +
                  ", r: " + r_or_rgb + ", g: " + g + ", b: " + b)

            self.__led_matrix[x][y][0] = r_or_rgb
            self.__led_matrix[x][y][1] = g
            self.__led_matrix[x][y][2] = b

    def get_pixel(self, x: int, y: int) -> List[int]:
        check_sense_hat_led_pixel_coordinates(x, y)

        pixel = self.__led_matrix[x][y]
        return [pixel[0], pixel[1], pixel[2]]

    def load_image(self, file_path: str, redraw: True):
        print("load_image: file_path: " +
              file_path + ", redraw: " + str(redraw))

    def clear(self, color=[0, 0, 0]) -> None:
        print("clear: color: " + str(color))

        for i in range(7):
            for j in range(7):
                pixel = self.__led_matrix[i][j]
                for k in range(3):
                    pixel[k] = color[k]

    def show_message(self, text_string: str, scroll_speed: float, text_color=[255, 255, 255], back_color=[0, 0, 0]) -> None:
        print("show_message: text_string: " + text_string + ", text_color: " +
              str(text_color) + ", back_color: " + str(back_color))

    def show_letter(self, s: str, text_color=[255, 255, 255], back_color=[0, 0, 0]) -> None:
        print("show_letter: s: " + s + ", text_color: " +
              str(text_color) + ", back_color: " + str(back_color))


def SenseHat():
    return SenseDummy()
