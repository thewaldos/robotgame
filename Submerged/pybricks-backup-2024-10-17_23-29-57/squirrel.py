from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop, Icon
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

def rocky(dbase:DriveBase):
    hub.system.set_stop_button(None)

    pressed = []
    hub.display.animate([Icon.EYE_LEFT_BLINK, Icon.EYE_RIGHT_BLINK], 500)
    while not any(pressed):
        pressed = hub.buttons.pressed()
        wait(10)
    hub.display.animate([Icon.EYE_LEFT_BROW_UP, Icon.EYE_RIGHT_BROW_UP, Icon.EYE_LEFT_BROW, Icon.EYE_RIGHT_BROW], 500)
    dbase.turn(360)
    hub.system.set_stop_button(Button.CENTER)