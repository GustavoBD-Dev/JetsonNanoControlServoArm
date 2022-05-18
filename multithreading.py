import threading
import time
from adafruit_servokit import ServoKit

# object to contorl servos
kit = ServoKit(channels=16)

def moveServo(servo, actualAnglePosition, newAnglePosition):
#kit.servo[0].angle = int(v)
    if newAnglePosition < actualAnglePosition:
        for i in range(actualAnglePosition, newAnglePosition - 1, -1):
            kit.servo[servo].angle = int(i)
            time.sleep(1/100)
    elif newAnglePosition > actualAnglePosition:
        for i in range(actualAnglePosition, newAnglePosition + 1, 1):
            kit.servo[servo].angle = int(i)
            time.sleep(1/100)


t0 = threading.Thread(name="Hilo_0", target=moveServo, args=(0, 90, 90, ))
t1 = threading.Thread(name="Hilo_1", target=moveServo, args=(1, 90, 26, ))
t2 = threading.Thread(name="Hilo_2", target=moveServo, args=(2, 90, 77, ))
t3 = threading.Thread(name="Hilo_3", target=moveServo, args=(3, 90, 95, ))
t4 = threading.Thread(name="Hilo_4", target=moveServo, args=(4, 90, 22, ))
t5 = threading.Thread(name="Hilo_5", target=moveServo, args=(5, 90, 90, ))

t0.start()
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()


