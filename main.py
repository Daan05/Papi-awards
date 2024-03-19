import RPi.GPIO as GPIO
import time
import math

# motor1
in1 = 1
in2 = 7
in3 = 8
in4 = 25
# motor2
in5 = 0
in6 = 11
in7 = 9
in8 = 10
# motor3
in9 = 26
in10 = 19
in11 = 13
in12 = 6

# careful lowering this, at some point you run into the mechanical limitation of how quick your motor can move
step_sleep = 0.002

#step_count = 4096 # 5.625*(1/64) per step, 4096 steps is 360°
direction = False # True for clockwise, False for counter-clockwise

# defining stepper motor sequence (found in documentation http://www.4tronix.co.uk/arduino/Stepper-Motors.php)
step_sequence = [[1,0,0,1],
                [1,0,0,0],
                [1,1,0,0],
                [0,1,0,0],
                [0,1,1,0],
                [0,0,1,0],
                [0,0,1,1],
                [0,0,0,1]]

# setting up
GPIO.setmode( GPIO.BCM )
GPIO.setwarnings(False)
GPIO.setup( in1, GPIO.OUT )
GPIO.setup( in2, GPIO.OUT )
GPIO.setup( in3, GPIO.OUT )
GPIO.setup( in4, GPIO.OUT )
GPIO.setup( in5, GPIO.OUT )
GPIO.setup( in6, GPIO.OUT )
GPIO.setup( in7, GPIO.OUT )
GPIO.setup( in8, GPIO.OUT )
GPIO.setup( in9, GPIO.OUT )
GPIO.setup( in10, GPIO.OUT )
GPIO.setup( in11, GPIO.OUT )
GPIO.setup( in12, GPIO.OUT )

# initializing
GPIO.output( in1, GPIO.LOW )
GPIO.output( in2, GPIO.LOW )
GPIO.output( in3, GPIO.LOW )
GPIO.output( in4, GPIO.LOW )
GPIO.output( in5, GPIO.LOW )
GPIO.output( in6, GPIO.LOW )
GPIO.output( in7, GPIO.LOW )
GPIO.output( in8, GPIO.LOW )
GPIO.output( in9, GPIO.LOW )
GPIO.output( in10, GPIO.LOW )
GPIO.output( in11, GPIO.LOW )
GPIO.output( in12, GPIO.LOW )

motor_pins1 = [in1,in2,in3,in4]
motor_pins2 = [in5,in6,in7,in8]
motor_pins3 = [in9,in10,in11,in12]

def cleanup():
    GPIO.output( in1, GPIO.LOW )
    GPIO.output( in2, GPIO.LOW )
    GPIO.output( in3, GPIO.LOW )
    GPIO.output( in4, GPIO.LOW )
    GPIO.output( in5, GPIO.LOW )
    GPIO.output( in6, GPIO.LOW )
    GPIO.output( in7, GPIO.LOW )
    GPIO.output( in8, GPIO.LOW )
    GPIO.output( in9, GPIO.LOW )
    GPIO.output( in10, GPIO.LOW )
    GPIO.output( in11, GPIO.LOW )
    GPIO.output( in12, GPIO.LOW )
    GPIO.cleanup()

def turnMotor2(degrees, direction):
    motor_pins = motor_pins2
    one_step = 0.087890625
    step_count = math.floor(degrees / 0.087890625)
    motor_step_counter = 0

    try:
        i = 0
        for i in range(step_count):
            for pin in range(0, len(motor_pins)):
                GPIO.output( motor_pins[pin], step_sequence[motor_step_counter][pin] )
            if direction==True:
                motor_step_counter = (motor_step_counter - 1) % 8
            elif direction==False:
                motor_step_counter = (motor_step_counter + 1) % 8
            else: # defensive programming
                print( "uh oh... direction should *always* be either True or False" )
                cleanup()
                exit( 1 )
            time.sleep( step_sleep )

    except KeyboardInterrupt:
        cleanup()
        exit( 1 )

def turnMotor1_3(degrees, direction):
    motor_pins1_ = motor_pins1
    motor_pins3_ = motor_pins3
    one_step = 0.087890625
    step_count = math.floor(degrees / one_step)
    motor_step_counter1 = 0
    motor_step_counter3 = 0

    try:
        i = 0
        for i in range(step_count):
            for pin in range(0, len(motor_pins1)):
                GPIO.output( motor_pins1_[pin], step_sequence[motor_step_counter1][pin] )
                GPIO.output( motor_pins3_[pin], step_sequence[motor_step_counter3][pin] )
            if direction==True:
                motor_step_counter1 = (motor_step_counter1 + 1) % 8
                motor_step_counter3 = (motor_step_counter3 + 1) % 8
            elif direction==False:
                motor_step_counter1 = (motor_step_counter1 - 1) % 8
                motor_step_counter3 = (motor_step_counter3 - 1) % 8
            else: # defensive programming
                print( "uh oh... direction should *always* be either True or False" )
                cleanup()
                exit( 1 )
            time.sleep( step_sleep )

    except KeyboardInterrupt:
        cleanup()
        exit( 1 )

def main():
# wacht tot 95 graden
# while temp < 95:
# time.sleep(1)

# motor2 omhoog(clockwise/counterclockwise) voor ... deg
# False = up, True = down
turnMotor2(360, False)

# motor1 clockwise, motor3 counterclockwise
turnMotor1_3(1080, True)

# motor2 omlaag() voor ... deg
turnMotor2(360, True)

# wacht 2 min
time.sleep(120)

# motor2 omhoog() voor ... deg
turnMotor2(360, False)

# motor1 clockwise, motor3 counterclockwise
turnMotor1_3(1080, True)

# motor2 omlaag() voor .. deg
turnMotor2(360, True)

# wacht 20 sec
time.sleep(20)

# motor2 omhoog
turnMotor2(360, True)

# motor1 counterclockwise, motor3 clockwise
turnMotor1_3(2160, False)

# motor 2 omlaag
turnMotor2(360, True)

main()
cleanup()
exit( 0 )
