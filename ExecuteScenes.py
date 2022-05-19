import threading
from adafruit_servokit import ServoKit
import csv
import time

# Read and get value steps to scenes from file
def getStepsScene(nameFile):
    with open(nameFile, 'r') as file:
        csv_reader = csv.reader(file, delimiter=',')
        # passing the csv_reader object to list 
        list_of_steps = list(csv_reader)
    return list_of_steps

# function to move servo - execute in thread
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

    """elif newAnglePosition == actualAnglePosition:
        kit.servo[servo].angle = int(newAnglePosition)"""
            

# create threads and send data to servos
def executeScene(scene):
    # loop betwen steps of scene
    for step in range(len(scene)):
        # if the values of position final step is in steps
        if step+1 < len(scene)-1:
            # set value of angles each servos
            print(scene[step][0], "- ", scene[step][1], "- ", scene[step][2], "- ", scene[step][3], "- ", scene[step][4], "- ", scene[step][5])
            servo0 = threading.Thread(name="Hilo_0", target=moveServo, args=(0, int(scene[step][0]), int(scene[step+1][0]), ))
            servo1 = threading.Thread(name="Hilo_1", target=moveServo, args=(1, int(scene[step][1]), int(scene[step+1][1]), ))
            servo2 = threading.Thread(name="Hilo_2", target=moveServo, args=(2, int(scene[step][2]), int(scene[step+1][2]), ))
            servo3 = threading.Thread(name="Hilo_3", target=moveServo, args=(3, int(scene[step][3]), int(scene[step+1][3]), ))
            servo4 = threading.Thread(name="Hilo_4", target=moveServo, args=(4, int(scene[step][4]), int(scene[step+1][4]), ))
            servo5 = threading.Thread(name="Hilo_5", target=moveServo, args=(5, int(scene[step][5]), int(scene[step+1][5]), ))
            # start threads
            servo0.start()
            servo1.start()
            servo2.start()
            servo3.start()
            servo4.start()
            servo5.start()
            # finish threads
            servo0.join()
            servo1.join()
            servo2.join()
            servo3.join()
            servo4.join()
            servo5.join()
# object to contorl servos
kit = ServoKit(channels=16)

# get steps of scene
scene =  getStepsScene('angleServosScene.csv')

# execute scene with the data of file
executeScene(scene)

    

    
    

