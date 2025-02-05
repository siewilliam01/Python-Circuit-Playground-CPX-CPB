import time
import math
from adafruit_circuitplayground import cp

while True:
    x, y, z = cp.acceleration
    x, y = float(x), float(y)
    
    angle = math.atan2(-y, -x)
    angle = (270+angle*180/(math.pi)) % 360
    print(angle)
    angle = int((angle)/36)
    
    magnitude = math.sqrt(x**2+y**2)
        
    cp.pixels[angle] = (3*magnitude, 0, 0)
    
    for i in range(10):
        if(i != angle):
            cp.pixels[i] = (0, 0, 0)
    
