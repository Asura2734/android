LED2_PIN = 27
Set up the GPIO pins as outputs
GPIO. setup (LED1_PIN, GPIO. OUT) 
GPIO. setup(LED2_PIN, GPIO. OUT) 
try:
    while True:
        Turn on LED 1 and turn off LED 2
        GPIO.output (LED1_PIN, GPIO. HIGH)
        GPIO. output (LED2_PIN, GPIO. LOW)
        print("LED 1 ON, LED 2 OFF")
        time.sleep (1)
        Turn off LED 1 and turn on LED 2
        GPIO. output (LED1_PIN, GPIO. LOW)

        time. sleep (1)
except KeyboardInterrupt:
    lean
    the GPIO settings before exiting
    GPIO. cleanup ()
    print ("Program exited cleanly")