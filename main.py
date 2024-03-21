import RPi.GPIO as GPIO
import time
import math

# motor2
in5 = 0
in6 = 11
in7 = 9
in8 = 10

dist = 20
on = 26
dirPin = 19


# careful lowering this, at some point you run into the mechanical limitation of how quick your motor can move
step_sleep = 0.002

#step_count = 4096 # 5.625*(1/64) per step, 4096 steps is 360°
#direction = False # True for clockwise, False for counter-clockwise

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
GPIO.setup( in5, GPIO.OUT )
GPIO.setup( in6, GPIO.OUT )
GPIO.setup( in7, GPIO.OUT )
GPIO.setup( in8, GPIO.OUT )
GPIO.setup(on, GPIO.OUT)
GPIO.setup(dirPin, GPIO.OUT)

# initializing
GPIO.output( in5, GPIO.LOW )
GPIO.output( in6, GPIO.LOW )
GPIO.output( in7, GPIO.LOW )
GPIO.output( in8, GPIO.LOW )
GPIO.output(on, GPIO.HIGH)
GPIO.output(dirPin, GPIO.LOW)

motor_pins2 = [in5,in6,in7,in8]

def cleanup():
    GPIO.output( in5, GPIO.LOW )
    GPIO.output( in6, GPIO.LOW )
    GPIO.output( in7, GPIO.LOW )
    GPIO.output( in8, GPIO.LOW )
    GPIO.output(on, GPIO.HIGH)
    GPIO.output(dirPin, GPIO.LOW)
    GPIO.cleanup()

def turnMotor(degrees, direction):
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
        
def move(t, direction):
    if direction:
        GPIO.output(dirPin, GPIO.LOW)
    else:
        GPIO.output(dirPin, GPIO.HIGH)
        
    for i in range(t):
        GPIO.output(on, GPIO.LOW)
        print("high")
        time.sleep(0.1)
    
    GPIO.output(on, GPIO.HIGH)
    GPIO.output(dirPin, GPIO.LOW)
    

def main():
  # wacht tot 95 graden
  # while temp < 95:
  # time.sleep(1)

  # motor2 omhoog(clockwise/counterclockwise) voor ... deg
  # False = up, True = down
  turnMotor(360, False)

  # motor1 clockwise, motor3 counterclockwise
  move(dist, False)

  # motor2 omlaag() voor ... deg
  turnMotor(360, True)

  # wacht 2 min
  time.sleep(120)

  # motor2 omhoog() voor ... deg
  turnMotor(360, False)

  # motor1 clockwise, motor3 counterclockwise
  move(dist, False)

  # motor2 omlaag() voor .. deg
  turnMotor(360, True)

  # wacht 20 sec
  time.sleep(20)


  # motor1 counterclockwise, motor3 clockwise
  move(2 * dist, True)


main()
cleanup()
exit( 0 )
