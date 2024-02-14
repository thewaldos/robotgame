from hub import light_matrix, motion_sensor, port
import hub
import runloop, motor, time, motor_pair, Top Hat

async def turnLeft():
    while motion_sensor.tilt_angles()[0]>-900:
        motor_pair.move(motor_pair.PAIR_1, -100)

    motor_pair.stop(motor_pair.PAIR_1)

async def main():
    motor_pair.unpair(motor_pair.PAIR_1);
    motor_pair.pair(motor_pair.PAIR_1, port.A, port.B);
    motion_sensor.set_yaw_face(motion_sensor.FRONT);
    motion_sensor.reset_yaw(0);    
    print(motion_sensor.tilt_angles()[0])
    await turnLeft();
    print(motion_sensor.tilt_angles()[0])

runloop.run(main());

quit(1);