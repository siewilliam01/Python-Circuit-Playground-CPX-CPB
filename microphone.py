import time
import math
from adafruit_circuitplayground import cp

while True:
    loudness = cp.sound_level
    print(loudness)
    loudness = loudness/50
    angle = int(loudness) % 10
    cp.pixels[angle] = (25, 0, 0)
    time.sleep(0.01)
    for i in range(10):
        if(i > angle):
            cp.pixels[i] = (0, 0, 0)
    
