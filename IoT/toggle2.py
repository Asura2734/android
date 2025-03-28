import RPi. GPIO as GPIO import time

GPIO. setmode (GPIO. BCM)

LED1 PIN = 17
LED_PIN = 27
GPIO. setup (LED1_PIN, GPIO. OUT) GPIO. setup (LED2_PIN, GPIO. OUT)

try:
    while True:
    Turn on LED 1 and turn off LED 2
    GPIO.output (LED1_PIN, GPIO. HIGH) 
    GPIO. output (LED2_PIN, GPIO. LOW) 
    print ("led 1 ON, Led 2 OFF")
    time. sleep (1)
    GPIO. output (LED1 PIN, GPIO. LOW)