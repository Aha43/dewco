import copy
import importlib
from typing import List

from ...commons import Raise
from ...util import get_env_var
from .color_map import ColorMap, ColorMapBuilder
from .data_validation import (check_list_of_rgb, check_rgb_list,
                              check_rgb_values,
                              check_sense_hat_led_pixel_coordinates)


class SenseFront:

    def __init__(self, sense_hat):

        self.sense_hat = sense_hat

        # Dummy environment defaults

        self.__dummy_humidity = 22.0
        self.__dummy_pressure = 50.0
        self.__dummy_temperature = 15.0  

        # LED      

        self.low_light = False
        if sense_hat != None:
            self.low_light = sense_hat.low_light
    
        self.__rotation = 0.0

        # LED matrix, used to simulate when dummy but also to hold given values
        # passed to frame buffer when fron for SenseHat API

        self.__led_matrix = []
        for i in range(64):
            self.__led_matrix.append([0, 0, 0])

    @classmethod
    def create_dummy_front(cls):
        return cls(None)

    @classmethod
    def from_env_settings(cls):
        dummy = get_env_var("__sense_hat_dummy__", "false")
        if dummy == "true": 
            return cls(None)
        sense_module = importlib.import_module("SenseHat")
        sense_hat = sense_module.SenseHat()
        return cls(sense_hat)


    def is_dummy(self) -> bool:
        return self.sense_hat == None

    # Environment

    def get_humidity(self):
        if self.sense_hat == None:
            return self.__dummy_humidity
        return self.sense_hat.get_humidity()

    def get_pressure(self):
        if self.sense_hat == None:
            return self.__dummy_pressure
        return self.sense_hat.get_pressure()

    def get_temperature(self):
        if self.sense_hat == None:
            return self.__dummy_temperature
        return self.sense_hat.get_temperature()

    def get_temperature_from_humidity(self):
        if self.sense_hat == None:
            return self.__dummy_temperature - 0.5
        return self.sense_hat.get_temperature_from_humidity()

    def get_temperature_from_pressure(self):
        if self.sense_hat == None:
            return self.__dummy_temperature + 0.5
        return self.sense_hat.get_temperature_from_pressure()

    # IMU

        # TODO :D

    # LED

    def f_set_low_light(self, v: bool) -> None:
        self.low_light = v
        if self.sense_hat != None:
            self.sense_hat.low_light = v

    def f_get_low_light(self) -> bool:
        if self.sense_hat != None:
            self.low_light = self.sense_hat.low_light
        return self.low_light

    def set_rotation(self, r: int, redraw: bool = True) -> None:
        print("set_rotation: " + str(r))
        self.__rotation = r
        if self.sense_hat != None:
            self.sense_hat.set_rotation(r, redraw)

    def f_get_rotation(self) -> int:
        return self.__rotation

    def flip_h(self, redraw: bool = True) -> None:
        print("flip_h: redraw: " + str(redraw))
        if self.sense_hat != None:
            self.sense_hat.flip_h(redraw)

    def flip_v(self, redraw: bool = True) -> None:
        print("flip_v: redraw: " + str(redraw))
        if self.sense_hat != None:
            self.sense_hat.flip_v(redraw)

    def set_pixels(self, pixels: List[List[int]]) -> None:
        Raise.if_not_of_length(pixels, 64, "pixels")
        check_list_of_rgb(pixels)
        
        if self.sense_hat != None:
            self.sense_hat.set_pixels(pixels)
        self.__led_matrix = copy.deepcopy(pixels)

    def get_pixels(self) -> List[List[int]]:
        if self.sense_hat != None:
            self.__led_matrix = self.sense_hat.get_pixels()
        return copy.deepcopy(self.__led_matrix)

    def f_get_pixels(self) -> List[List[int]]:
        return copy.deepcopy(self.__led_matrix)

    def set_pixel(self, x: int, y: int, r_or_rgb, g: int = None, b: int = None) -> None:
        check_sense_hat_led_pixel_coordinates(x, y)

        array_pos = x * 8 + y

        if g == None and b == None:
            check_rgb_list(r_or_rgb)

            print("set_pixel: x: " + str(x) + ", y: " +
                  str(y) + ", rgb: " + str(r_or_rgb))

            if self.sense_hat != None:
                self.sense_hat.set_pixel(x, y, r_or_rgb)

            self.__led_matrix[array_pos][0] = r_or_rgb[0]
            self.__led_matrix[array_pos][1] = r_or_rgb[1]
            self.__led_matrix[array_pos][2] = r_or_rgb[2]

        else:
            check_rgb_values(r_or_rgb, g, b)

            print("set_pixel: x: " + str(x) + ", y: " + str(y) +
                  ", r: " + str(r_or_rgb) + ", g: " + str(g) + ", b: " + str(b))

            if self.sense_hat != None:
                self.sense_hat.set_pixel(x, y, r_or_rgb, g, b)

            self.__led_matrix[array_pos][0] = r_or_rgb
            self.__led_matrix[array_pos][1] = g
            self.__led_matrix[array_pos][2] = b

    def get_pixel(self, x: int, y: int) -> List[int]:
        check_sense_hat_led_pixel_coordinates(x, y)

        array_pos = x * 8 + y

        pixel = []
        if self.sense_hat != None:
            pixel = self.sense_hat(x, y)
            self.__led_matrix[array_pos] = pixel

        return self.__led_matrix[array_pos]

    def f_get_pixel(self, x: int, y: int) -> List[int]:
        check_sense_hat_led_pixel_coordinates(x, y)

        array_pos = x * 8 + y

        return self.__led_matrix[array_pos]

    def f_get_color_map(self, use_front_matrix: bool) -> ColorMap:

        matrix = []
        if use_front_matrix:
            matrix = self.f_get_pixels()
        else:
            matrix = self.get_pixels()

        builder = ColorMapBuilder()
        builder.append_pixels(matrix)

        return builder.build()

    def f_set_color_map(self, map: ColorMap) -> None:
        self.set_pixels(map.get_matrix())

    def load_image(self, file_path: str, redraw: True):
        print("load_image: file_path: " +
              file_path + ", redraw: " + str(redraw))

    def clear(self, color=[0, 0, 0]) -> None:
        print("clear: color: " + str(color))

        if self.sense_hat != None:
            self.sense_hat.clear(color)
        
        for i in range(64):
            self.__led_matrix[i] = color.copy()

    def show_message(self, text_string: str, scroll_speed: float, text_color=[255, 255, 255], back_color=[0, 0, 0]) -> None:
        print("show_message: text_string: " + text_string + ", text_color: " +
              str(text_color) + ", back_color: " + str(back_color))

        if self.sense_hat != None:
            self.sense_hat.show_message(text_string, scroll_speed, text_color, back_color)
            self.get_pixels()

    def show_letter(self, s: str, text_color=[255, 255, 255], back_color=[0, 0, 0]) -> None:
        print("show_letter: s: " + s + ", text_color: " +
              str(text_color) + ", back_color: " + str(back_color))

        if self.sense_hat != None:
            self.sense_hat.show_letter(s, text_color, back_color)
            self.get_pixels()
