class SenseDummy:
    """Fallback dummy api for the SenseHat API when nor a real Sense HAT system or emulator is avaliable"""
    def get_humidity(self):
        return 22.0

def SenseHat():
    return SenseDummy()
