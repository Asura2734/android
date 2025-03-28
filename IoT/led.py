import RPL. GPIO as GPIO
import time
GPIO, setwarnings (False)
GPIO, setmode (GPIO.BCM)
GPIO, setup (4, GPIO.OUT)

while True:
    GPTO, output (4, GPIO. HIGH)
    time. sleep (1)
    GPIO. output (4, GPIO. LOW)
    time. sleep (1)