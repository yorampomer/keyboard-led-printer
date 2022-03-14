from evdev import InputDevice, list_devices, ecodes, categorize
import time

CODE_MAP_CHAR = {
    'KEY_MINUS': "-",
    'KEY_SPACE': " ",
    'KEY_U': "U",
    'KEY_W': "W",
    'KEY_BACKSLASH': "\\",
    'KEY_GRAVE': "`",
    'KEY_NUMERIC_STAR': "*",
    'KEY_NUMERIC_3': "3",
    'KEY_NUMERIC_2': "2",
    'KEY_NUMERIC_5': "5",
    'KEY_NUMERIC_4': "4",
    'KEY_NUMERIC_7': "7",
    'KEY_NUMERIC_6': "6",
    'KEY_NUMERIC_9': "9",
    'KEY_NUMERIC_8': "8",
    'KEY_NUMERIC_1': "1",
    'KEY_NUMERIC_0': "0",
    'KEY_E': "E",
    'KEY_D': "D",
    'KEY_G': "G",
    'KEY_F': "F",
    'KEY_A': "A",
    'KEY_C': "C",
    'KEY_B': "B",
    'KEY_M': "M",
    'KEY_L': "L",
    'KEY_O': "O",
    'KEY_N': "N",
    'KEY_I': "I",
    'KEY_H': "H",
    'KEY_K': "K",
    'KEY_J': "J",
    'KEY_Q': "Q",
    'KEY_P': "P",
    'KEY_S': "S",
    'KEY_X': "X",
    'KEY_Z': "Z",
    'KEY_KP4': "4",
    'KEY_KP5': "5",
    'KEY_KP6': "6",
    'KEY_KP7': "7",
    'KEY_KP0': "0",
    'KEY_KP1': "1",
    'KEY_KP2': "2",
    'KEY_KP3': "3",
    'KEY_KP8': "8",
    'KEY_KP9': "9",
    'KEY_5': "5",
    'KEY_4': "4",
    'KEY_7': "7",
    'KEY_6': "6",
    'KEY_1': "1",
    'KEY_0': "0",
    'KEY_3': "3",
    'KEY_2': "2",
    'KEY_9': "9",
    'KEY_8': "8",
    'KEY_LEFTBRACE': "[",
    'KEY_RIGHTBRACE': "]",
    'KEY_COMMA': ",",
    'KEY_EQUAL': "=",
    'KEY_SEMICOLON': ";",
    'KEY_APOSTROPHE': "'",
    'KEY_T': "T",
    'KEY_V': "V",
    'KEY_R': "R",
    'KEY_Y': "Y",
    'KEY_TAB': "\t",
    'KEY_DOT': ".",
    'KEY_SLASH': "/",
}


def parse_key_to_char(val):
    return CODE_MAP_CHAR[val] if val in CODE_MAP_CHAR else ""


class Scanner:
    def __init__(self):
        self._scanner = None


    def _set_scanner(self):
        devices = [InputDevice(fn) for fn in list_devices()]
        scanners = [device for device in devices if device.name == 'SCANNER SCANNER         ']
        if len(scanners) == 0:
            raise OSError("No scanners")
        scanner = scanners[0]
        scanner.grab()
        self._scanner = scanner

    def get_barcode(self):
        while True:
            try:
                barcode = ""
                if self._scanner is None:
                    self._set_scanner()

                for event in self._scanner.read_loop():
                    if event.type == ecodes.EV_KEY:
                        e = categorize(event)
                        if e.keystate == e.key_down:
                            if e.keycode == "KEY_ENTER":
                                return barcode
                            barcode += parse_key_to_char(e.keycode)
            except OSError:
                print("Scanner error, trying again")
                time.sleep(0.5)
                self._scanner = None
