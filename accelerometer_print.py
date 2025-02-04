import time
import math
from adafruit_circuitplayground import cp

while True:
    x, y, z = cp.acceleration
    x, y, z = float(x), float(y), float(z)
    angle = math.atan2(-y, -x)
    angle = angle*180/(math.pi)
    magnitude = math.sqrt(x**2+y**2)
    print(angle, magnitude)
    angle = int((270+angle)/36)
    angle = angle % 10
    cp.pixels[angle] = (5*magnitude, 0, 0)
    for i in range(10):
        if(i != angle):
            cp.pixels[i] = (0, 0, 0)            
    time.sleep(0.01)

