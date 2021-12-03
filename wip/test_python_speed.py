import time
import RPi.GPIO as GPIO

def cleanup():
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.LOW)
    GPIO.output(in3, GPIO.LOW)
    GPIO.output(in4, GPIO.LOW)
    GPIO.cleanup()


min_wait_time = 0.0007

in1 = 18
in2 = 23
in3 = 24
in4 = 25

step_sequence = [[1, 0, 0, 1],
                 [1, 0, 0, 0],
                 [1, 1, 0, 0],
                 [0, 1, 0, 0],
                 [0, 1, 1, 0],
                 [0, 0, 1, 0],
                 [0, 0, 1, 1],
                 [0, 0, 0, 1]]


GPIO.setmode(GPIO.BCM)
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(in3, GPIO.OUT)
GPIO.setup(in4, GPIO.OUT)

# initializing
GPIO.output(in1, GPIO.LOW)
GPIO.output(in2, GPIO.LOW)
GPIO.output(in3, GPIO.LOW)
GPIO.output(in4, GPIO.LOW)

motor_pins = [in1, in2, in3, in4]

direction = True
motor_step_counter = 0

start_time = time.time()

for i in range(0, 4096):
    for pin in range(0, len(motor_pins)):
        GPIO.output(motor_pins[pin], step_sequence[motor_step_counter][pin])
        pass

    if direction == True:
        motor_step_counter = (motor_step_counter - 1) % 8
    elif direction == False:
        motor_step_counter = (motor_step_counter + 1) % 8
    else:  # defensive programming
        print("uh oh... direction should *always* be either True or False")
        cleanup()
        exit(1)

    time.sleep(min_wait_time)

    pass

print("--- %s seconds ---" % (time.time() - start_time))

cleanup()

