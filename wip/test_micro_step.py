import time
import RPi.GPIO as GPIO
from pprint import pprint
from statistics import mean


def main():

    min_wait_time_physical = 0.00075
    min_wait_time = min_wait_time_physical / 1
    bits = 4
    micro_steps = 2**bits

    micro_step_length = min_wait_time / micro_steps

    used_motors = [0]

    step_count = 4096  # 5.625*(1/64) per step, 4096 steps is 360°
    step_count = 2
    direction = False  # True for clockwise, False for counter-clockwise

    step_sequence = [[1, 0, 0, 1],
                     [1, 0, 0, 0],
                     [1, 1, 0, 0],
                     [0, 1, 0, 0],
                     [0, 1, 1, 0],
                     [0, 0, 1, 0],
                     [0, 0, 1, 1],
                     [0, 0, 0, 1]]

    in1 = 18
    in2 = 23
    in3 = 24
    in4 = 25

    mp1 = 12
    mp2 = 16
    mp3 = 20
    mp4 = 21

    motor_pins = [in1, in2, in3, in4]

    if True:
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(in1, GPIO.OUT)
        GPIO.setup(in2, GPIO.OUT)
        GPIO.setup(in3, GPIO.OUT)
        GPIO.setup(in4, GPIO.OUT)
        GPIO.setup(mp1, GPIO.OUT)
        GPIO.setup(mp2, GPIO.OUT)
        GPIO.setup(mp3, GPIO.OUT)
        GPIO.setup(mp4, GPIO.OUT)

    if True:
        # initializing
        GPIO.output(in1, GPIO.LOW)
        GPIO.output(in2, GPIO.LOW)
        GPIO.output(in3, GPIO.LOW)
        GPIO.output(in4, GPIO.LOW)
        GPIO.output(mp1, GPIO.LOW)
        GPIO.output(mp2, GPIO.LOW)
        GPIO.output(mp3, GPIO.LOW)
        GPIO.output(mp4, GPIO.LOW)

    def cleanup():
        GPIO.output(in1, GPIO.LOW)
        GPIO.output(in2, GPIO.LOW)
        GPIO.output(in3, GPIO.LOW)
        GPIO.output(in4, GPIO.LOW)
        GPIO.output(mp1, GPIO.LOW)
        GPIO.output(mp2, GPIO.LOW)
        GPIO.output(mp3, GPIO.LOW)
        GPIO.output(mp4, GPIO.LOW)
        GPIO.cleanup()

    def create_exec_array():
        motor_step_counter = 0
        arr = []
        i = 0
        for i in range(step_count):
            for motor in range(micro_steps):
                micro_step = (motor,[])
                if motor in used_motors:
                    for pin in range(0, len(motor_pins)):
                        #GPIO.output(motor_pins[pin], step_sequence[motor_step_counter][pin])
                        micro_step[1].append(step_sequence[motor_step_counter][pin])
                        #print(motor_pins[pin], step_sequence[motor_step_counter][pin])

                    if direction == True:
                        motor_step_counter = (motor_step_counter - 1) % 8
                    elif direction == False:
                        motor_step_counter = (motor_step_counter + 1) % 8
                else:
                    pass
                #print(micro_step)
                arr.append(micro_step)
        #pprint(arr)
        return arr

    def sleep(duration, get_now=time.perf_counter):
        now = get_now()
        end = now + duration
        while now < end:
            now = get_now()

    def exec_array(arr):
        out_timer = []
        for ms in arr:
            mot = ms[0]
            if mot in used_motors:
                for pin in range(0, 4):
                    GPIO.output(motor_pins[pin], ms[1][pin])
                    pass
                out_timer.append(time.time())
            else:
                pass

            #time.sleep(micro_step_length)
            sleep(micro_step_length)
        return out_timer

        pass

    arr = create_exec_array()
    pprint(arr)
    for i in range(10):
        start_time = time.time()
        timer = exec_array(arr)
        #print(timer)

        print("--- %s seconds ---" % (time.time() - start_time))
        sleep(0.2)

    diffs = [timer[i+1] - timer[i] for i in range(0,len(timer)-1)]
    print(diffs)
    print(mean(diffs))
    print(min_wait_time_physical)
    print('%6f' % min_wait_time)


    cleanup()





if __name__ == '__main__':
    main()