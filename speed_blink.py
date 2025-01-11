# Save on CPX/CPB as code.py
# Blinks the top right RED LED
import board
import digitalio
import time

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

def main():
    x = 0
    while True:
        x=x+1
        led.value=True
        time.sleep(5/x)
        led.value=False
        time.sleep(5/x)
        print(x)

main()