import time
import math
from adafruit_circuitplayground import cp

data_smoothing_scale = 100

while True:
    x, y, z = cp.acceleration
    x, y, z = data_smoothing_scale*x, data_smoothing_scale*y, data_smoothing_scale*z
    x, y, z = int(x), int(y), int(z)
    x, y, z = x/data_smoothing_scale, y/data_smoothing_scale, z/data_smoothing_scale
    angle = math.atan2(-y, -x)
    angle = 180 + angle*180/(math.pi)
    magnitude = math.sqrt(x**2+y**2)
    print(angle, magnitude)

    time.sleep(0.01)

