from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

def boris(dbase:DriveBase, sbam:Motor, pam:Motor):    
    dbase.straight(500, then=Stop.BRAKE, wait=False)
    sbam.run_angle(100, 180, wait=False)
    pam.run_time(100, 2000, wait=True)
    dbase.turn(180)
    dbase.straight(500)
def natasha(dbase:DriveBase,sbam:Motor, pam:Motor):
    dbase.straight(500, then=Stop.BRAKE, wait=True)
    dbase.turn(180, wait=False)
    sbam.run_angle(100, 180, wait=False)
    pam.run_time(100, 2000, wait=True)
    dbase.straight(500)