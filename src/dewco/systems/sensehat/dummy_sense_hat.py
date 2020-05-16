class SenseDummy:
    """Fallback dummy api for the SenseHat API when nor a real Sense HAT system or emulator is avaliable"""

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
    def show_letter(self, s: str, text_color = [255, 255, 255], back_color = [255, 255, 255]) -> None:
        print("show on LED letter: " + s)
        return None

def SenseHat():
    return SenseDummy()
