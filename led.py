from rpi_ws281x import Adafruit_NeoPixel, Color
import time
from word_to_array import word_to_array
import numpy as np

# LED strip configuration:
LED_COUNT = 8 * 32  # Number of LED pixels.
LED_PIN = 18  # GPIO pin connected to the pixels (18 uses PWM!).
# LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10  # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255  # Set to 0 for darkest and 255 for brightest
LED_INVERT = False  # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 0  # set to '1' for GPIOs 13, 19, 41, 45 or 53


class Led:
    def __init__(self):
        self._strip = None

    @staticmethod
    def _color_wipe(strip, color, wait_ms=0):
        """Wipe color across display a pixel at a time."""
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, color)
            if wait_ms:
                time.sleep(wait_ms / 1000.0)
            strip.show()

    def clear(self):
        strip = self._get_strip()
        self._color_wipe(strip, Color(0, 0, 0))

    def _get_strip(self):
        while True:
            try:
                if self._strip is not None:
                    return self._strip
                strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS,
                                          LED_CHANNEL)
                strip.begin()
                self._strip = strip
                self.clear()
                return self._strip
            except Exception:
                print("failed to get strip")
                time.sleep(0.5)

    def print_word(self, word):
        strip = self._get_strip()
        self._color_wipe(strip, Color(0, 0, 0), 10)
        arr = word_to_array(word)

        scrolling = len(arr[0]) - 32
        for s in range(0, scrolling, 2):
            split = arr[:,s:-1]
            it = np.nditer(split, flags=['f_index'])
            for i in it:
                if it.index <= LED_COUNT:
                    if i:
                        strip.setPixelColor(it.index, Color(10, 10, 10))
                    else:
                        strip.setPixelColor(it.index, Color(0, 0, 0))
            strip.show()
            time.sleep(0.5)
