from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch


def bullwinkle(dbase:DriveBase):
    dbase.settings(500, 700,250,350)
    dbase.straight(2000)
    dbase.turn(180)
    dbase.straight(2000)
    dbase.turn(-180)
    