FROM python:3.8
RUN apt-get update && apt-get install -y gcc make build-essential python-dev git scons swig python3-rpi.gpio
RUN pip3 install adafruit-circuitpython-neopixel rpi_ws281x numpy
RUN pip3 install evdev Pillow
COPY main.py /opt/main.py
COPY led.py /opt/led.py
COPY scanner.py /opt/scanner.py
COPY word_to_array.py /opt/word_to_array.py
COPY Cascadia.ttf /opt/Cascadia.ttf
COPY mapping.txt /opt/mapping.txt
COPY unknown.txt /opt/unknown.txt
WORKDIR /opt
CMD python3 ./main.py
