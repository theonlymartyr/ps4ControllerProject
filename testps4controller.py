#######################################################
# Author: Jacob Kubanek
# Created: 5/25/22
# Modified: 5/25/22
# Description: Proof of concept project for managing
# and using ps4 controller inputs on Raspberry pi with
# a potential future project of controlling a vehicle.
# TODO:
#    -Map out desired control scheme
#    -Figure out how to output relevant information to
#     some sort of controller for gas/brake/steering
#######################################################
from pyPS4Controller.controller import Controller
from pyPS4Controller.event_mapping.DefaultMapping import DefaultMapping

brakePressed = False
cruiseSet = False
speed = 0
cruiseSpeed = 0

class MyController(Controller):
    ##########################################
    # -Axis values are a 32 bit signed int
    #  so we can divide by 32767 to get a value
    #  between 0 & 1
    # -Trigger values are a 32 bit signed int
    #  so we add 32767 and divide by 65534 to
    #  get a value between 0 & 1. 50% press on
    #  trigger is 0, 0-25% is negative, 50+%
    #  is positve otherwise
    ##########################################
    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)
    def on_L3_up(self, value):
       print(value/32767)
    def on_L3_down(self, value):
       print(value/32767)
    ####################################
    # R2 will be used as the accelerator
    ####################################
    def on_R2_press(self, value):
       global speed, cruiseSpeed
       speed = (value+32767)/65534
       if not cruiseSet:
           cruiseSpeed = speed
       print("Speed: " + str(speed))
       print("Cruise: " + str(cruiseSpeed))
    ###################################
    # Do we want to do anything on accelerator release?
    ###################################
    def on_R2_release(self):
       pass 
    def on_L2_press(self, value):
       global cruiseSet
       if cruiseSet:
           cruiseSet = False
       print(value/32767)
    def on_L2_release(self):
       pass
    def on_triangle_press(self):
       global cruiseSet, speed, cruiseSpeed
       cruiseSet = True
       cruiseSpeed = speed
       print("Cruise Set")
    def on_square_press(self):
       global cruiseSet
    def on_circle_press(self):
       global cruiseSet, speed, cruiseSpeed
       cruiseSet = False
       cruiseSpeed = speed
    def on_circle_release(self):
       brakePressed = False
    #####################################################################
    # Everything defined below is just to prevent printed output for now
    #####################################################################
    def on_L3_left(self, value):
       pass
    def on_L3_right(self, value):
       pass
    def on_triangle_release(self):
       pass
    def on_square_release(self):
       pass
    def on_R3_left(self, value):
       pass
    def on_R3_right(self, value):
       pass
controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)
controller.debug = False
###########################################
# Nothing executes after the listen command
# All logic needs to be above
###########################################
controller.listen(timeout=60)
