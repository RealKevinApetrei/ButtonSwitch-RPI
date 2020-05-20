import RPi.GPIO as GPIO

ledPinGreen = 11 # Define LedPin 1
ledPinRed = 12 # Define LedPin 2
buttonPin = 16 # Define ButtonPin

ledStateGreen = True
ledStateRed = False

def setup():
    GPIO.setmode(GPIO.BOARD)

    GPIO.setup(ledPinGreen, GPIO.OUT)
    GPIO.setup(ledPinRed, GPIO.OUT)

    GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def buttonEvent(channel):
    global ledStateGreen
    global ledStateRed

    print("ButtonEvent --> GPIO{}".format(channel))

    ledStateGreen = not ledStateGreen
    ledStateRed = not ledStateRed

    if ledStateGreen:
        print("LEDEvent --> GPIO{}".format(ledPinGreen))
    elif ledStateRed:
        print("LEDEvent --> GPIO{}".format(ledPinRed))


    GPIO.output(ledPinGreen, ledStateGreen)
    GPIO.output(ledPinRed, ledStateRed)

def loop():
    GPIO.add_event_detect(buttonPin, GPIO.FALLING, callback=buttonEvent, bouncetime=300)

    while True:
        pass

def destroy():
    GPIO.cleanup()

if __name__ == "__main__":
    print("Program Starting...")

    setup()

    try:
        loop()
    except KeyboardInterrupt:
        destroy()
