FROM python:3.8
RUN apt-get update && apt-get install -y gcc make build-essential python-dev git scons swig python3-rpi.gpio
RUN pip3 install adafruit-circuitpython-neopixel rpi_ws281x 
COPY main.py /opt/main.py
CMD python3 /opt/main.py
