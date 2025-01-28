import time
from adafruit_circuitplayground import cp

data_smoothing_scale = 100

while True:
    x, y, z = cp.acceleration
    x, y, z = data_smoothing_scale*x, data_smoothing_scale*y, data_smoothing_scale*z
    x, y, z = int(x), int(y), int(z)
    x, y, z = x/data_smoothing_scale, y/data_smoothing_scale, z/data_smoothing_scale
    print(x, y, z)

    time.sleep(0.01)
