import time
from scanner import Scanner
from led import Led
from word_to_array import word_to_array

def load_mapping():
    while True:
        try:
            with open("mapping.txt") as f:
                text = f.read()
            lines = text.splitlines()
            split = [line.split(",") for line in lines]
            mapping = dict(split)
            print(mapping)
            return mapping
        except Exception as e:
            print(f"Mapping loading failed")
            print(e)
            time.sleep(0.5)


# Main program logic follows:
if __name__ == '__main__':
    word_to_array("Welcome")
    try:
        led = Led()
        led.clear()
        led.print_word("Welcome")
        time.sleep(0.5)
        led.clear()
        mapping = load_mapping()
        scanner = Scanner()
        while True:
            barcode = scanner.get_barcode()
            print(barcode)
            if barcode in mapping:
                mapped = mapping[barcode]
            else:
                mapped = "unknown"
            print(mapped)
            led.print_word(mapped)
            time.sleep(2)
            led.clear()
    except KeyboardInterrupt:
        led.clear()