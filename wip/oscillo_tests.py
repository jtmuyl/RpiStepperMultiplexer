import time
import RPi.GPIO as GPIO
from pprint import pprint
from statistics import mean


def sleep(duration, get_now=time.perf_counter):
    now = get_now()
    end = now + duration
    while now < end:
        now = get_now()


def main():

    sleeper = 0.00075

    GPIO.cleanup()

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(6, GPIO.OUT)
    GPIO.output(6, GPIO.LOW)

    print("expected frequency: %2f" % ((1/sleeper)/2))

    while True:
        GPIO.output(6, GPIO.LOW)
        sleep(sleeper)
        GPIO.output(6, GPIO.HIGH)
        sleep(sleeper)



    pass

def set_high():
    GPIO.cleanup()

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(6, GPIO.OUT)
    GPIO.output(6, GPIO.HIGH)



if __name__ == '__main__':
    #main()
    set_high()
