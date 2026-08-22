import time

import RPi.GPIO as GPIO

PIN = 18


def main():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(PIN, GPIO.OUT)

    try:
        while True:
            GPIO.output(PIN, GPIO.HIGH)
            print("Pin High")
            time.sleep(0.5)
            GPIO.output(PIN, GPIO.LOW)
            print("Pin Low")
            time.sleep(0.5)
    except KeyboardInterrupt:
        print("Exiting Program")
    finally:
        GPIO.cleanup()


if __name__ == "__main__":
    main()
