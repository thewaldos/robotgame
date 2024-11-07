from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

def Brucey(dbase:DriveBase, sbam:Motor, pam:Motor):
    dbase.settings(300, 700,250,500)
    pam.run_angle(130,43, wait=False)
    dbase.straight(860)
    dbase.turn(-56)
    dbase.straight(60)
    dbase.straight(-180)
    dbase.turn(-38,then=Stop.BRAKE)
    dbase.straight(100)
    pam.run_angle(105,25)
    dbase.straight(-150)