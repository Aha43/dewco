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

    #LED
    def clear(self, color = [0, 0, 0]) -> None:
        print("clear: color: " + list_to_str(color))

    def set_rotation(self, r: int, redraw: bool = True) -> None:
        print("set_rotation: " + str(r))

    def show_letter(self, s: str, text_color = [255, 255, 255], back_color = [255, 255, 255]) -> None:
        print("show_letter: " + s + ", text_color: " + list_to_str(text_color) + ", back_color: " + list_to_str(back_color))

def SenseHat():
    return SenseDummy()
