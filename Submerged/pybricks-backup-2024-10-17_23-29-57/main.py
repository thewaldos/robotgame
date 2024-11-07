from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop, Icon
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, hub_menu, multitask, run_task
import moose, squirrel
from BruceInTheReef import Brucey
from spy import boris, natasha

# Build your robot  in the code 
hub = PrimeHub()
leftDriveMotor = Motor(Port.E, Direction.COUNTERCLOCKWISE)
rightDriveMotor = Motor(Port.F)
leftAttMotor = Motor(Port.B)
rightAttMotor = Motor(Port.A)
ears = UltrasonicSensor(Port.C)
eyes = ColorSensor(Port.D) 


# 56mm wheel diameter. 128mm track
mavro = DriveBase(leftDriveMotor, rightDriveMotor, wheel_diameter=56, axle_track=128)
mavro.use_gyro(True)


def main():  
    # Turn off the "stop" function of the center button 
    hub.system.set_stop_button(None)

    # Blink the center button light
    hub.light.animate([Color.RED, Color.ORANGE, Color.GREEN, Color.BLUE], interval=250)
    
    # This is a collection variable. We will use it to store the collection "pressed" buttons
    pressed = []

    # brightness variable is a collection we can cycle through. It creates a list of brightness levels
    brightness = list(range(0, 100, 4)) + list(range(100, 0, -4))

    # This will make the PAUSE icon pulse with brightness
    hub.display.animate([Icon.PAUSE * i / 100 for i in brightness], 30)

    # Here, we're checking the "pressed" collection to see if anything is in it.
    # While it is empty, we're just going to keep checking it in a loop
    # Once a button is pressed, it is no longer empty and we proceed on to the code after the wait(10)
    while not any(pressed):
        #and here, we're adding any butttons that are being pressed to it
        pressed = hub.buttons.pressed()
        wait(10) # without this, the code moves faster than it can detect buttons

    # turn the Center button back into a stop button.
    hub.system.set_stop_button(Button.CENTER) 
    
    # this holds the mission value so we can keep recreating the menu until we exit
    mission = ""
    # The X mission is an exit key, otherwise after each mission completes, it goes right back to menu
    while mission != "X":
        # this built in function lets you pick from the options
        theMenu = hub_menu("B", "N", "X")
        mission = theMenu
        if mission =="B":
            Brucey(mavro, rightAttMotor, leftAttMotor)
        elif mission == "S":
            squirrel.rocky(mavro)
        elif mission == "N":
            natasha(mavro, rightAttMotor, leftAttMotor)

main()