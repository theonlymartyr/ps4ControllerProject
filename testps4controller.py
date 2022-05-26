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




class MyController(Controller):
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
       print(value/32767)
    ###################################
    # Do we want to do anything on accelerator release?
    ###################################
    def on_R2_release(self):
       print("accelerator released")
    def on_L2_press(self, value):
       global cruiseSet
       if cruiseSet:
           cruiseSet = False
       print(value/32767)
    def on_L2_release(self):
       pass
       #print("Stop Braking")
    def on_triangle_press(self):
       global cruiseSet
       cruiseSet = True
    def on_square_press(self):
       global cruiseSet
       #cruiseSet = False
    def on_circle_press(self):
       global brakePressed
       #brakePressed = True
    def on_circle_release(self):
       brakePressed = False
#####################################################################
# I want to ignore left/right for now, so they need to be overwritten
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
