from machine import Pin
import time

gpio_pins = [20, 19, 18, 15, 14, 13, 12] # gpios used to drive 7 segment LED

# define what to output on each segment for each number
PINS = [
    [1,1,1,1,1,0,1], #0
    [0,1,1,0,0,0,0], #1
    [1,1,0,1,1,1,0], #2
    [1,1,1,1,0,1,0], #3
    [0,1,1,0,0,1,1], #4
    [1,0,1,1,0,1,1], #5
    [1,0,1,1,1,1,1], #6
    [1,1,1,0,0,0,0], #7
    [1,1,1,1,1,1,1], #8
    [1,1,1,1,0,1,1] #9
    ]

gpio_objects = [Pin(pin, Pin.OUT) for pin in gpio_pins] # define each gpio as an output

while(1):
    for list_of_pins in PINS: # iterate through each element of PINS, for each number
        counter = 0 # counter to link each segment to a gpio
        for gpio in gpio_objects:
            gpio.value(list_of_pins[counter])
            counter += 1
        time.sleep(1) # a second pause to update each number