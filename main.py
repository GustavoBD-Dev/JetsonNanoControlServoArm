# from ast import Try
import cv2
import numpy as np
import calcular_tres
import time
import asyncio
import threading
from progress.bar import Bar
# from adafruit_servokit import ServoKit
import csv
import time

# Read and get value steps to scenes from file


def getStepsScene(nameFile):
    with open(nameFile, 'r') as file:
        csv_reader = csv.reader(file, delimiter=',')
        # passing the csv_reader object to list
        list_of_steps = list(csv_reader)
    return list_of_steps


"""
# function to move servo - execute in thread
def moveServo(servo, actualAnglePosition, newAnglePosition):

  # object to contorl servos
  kit = ServoKit(channels=16)
  if newAnglePosition < actualAnglePosition:
    for i in range(actualAnglePosition, newAnglePosition - 1, -1):
      kit.servo[servo].angle = int(i)
      time.sleep(1/100)

  elif newAnglePosition > actualAnglePosition:
    for i in range(actualAnglePosition, newAnglePosition + 1, 1):
      kit.servo[servo].angle = int(i)
      time.sleep(1/100)


# create threads and send data to servos
def executeScene(scene):
    # loop betwen steps of scene
    for step in range(len(scene)):
        # if the values of position final step is in steps
        if step+1 < len(scene)-1:
            # set value of angles each servos
            print(scene[step][0], "- ", scene[step][1], "- ", scene[step][2],
                  "- ", scene[step][3], "- ", scene[step][4], "- ", scene[step][5])
            servo0 = threading.Thread(name="Hilo_0", target=moveServo, args=(
                0, int(scene[step][0]), int(scene[step+1][0]), ))
            servo1 = threading.Thread(name="Hilo_1", target=moveServo, args=(
                1, int(scene[step][1]), int(scene[step+1][1]), ))
            servo2 = threading.Thread(name="Hilo_2", target=moveServo, args=(
                2, int(scene[step][2]), int(scene[step+1][2]), ))
            servo3 = threading.Thread(name="Hilo_3", target=moveServo, args=(
                3, int(scene[step][3]), int(scene[step+1][3]), ))
            servo4 = threading.Thread(name="Hilo_4", target=moveServo, args=(
                4, int(scene[step][4]), int(scene[step+1][4]), ))
            servo5 = threading.Thread(name="Hilo_5", target=moveServo, args=(
                5, int(scene[step][5]), int(scene[step+1][5]), ))
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
            servo5.join()"""


def runScene(script):

    print("Execute escene to : ", script)
    # get steps of scene
    scene = getStepsScene('angleServosScene.csv')

    # execute scene with the data of file
    time.sleep(13)  # executeScene(scene)

    print("Scene completed!!!", script)


def dibujar(mask, color):
  colorDetectado = False
  contornos, hierachy = cv2.findContours(
      mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
  for c in contornos:
    area = cv2.contourArea(c)
    if area > 3000:
        x, y, w, h = cv2.boundingRect(c)
        if color == (255, 0, 0):
            cv2.rectangle(frame, (x, y), (x+w, y+h), color, 3)
            cv2.putText(frame, 'Azul', (x-10, y-10),
                        font, 0.75, color, 2, cv2.LINE_AA)
            print("azul")
            colorDetectado = True
            runScene("BLUE")
        # arduino.write(cad.encode('ascii'))
        elif color == (0, 255, 0):
            cv2.rectangle(frame, (x, y), (x+w, y+h), color, 3)
            cv2.putText(frame, 'Verde', (x-10, y-10),
                        font, 0.75, color, 2, cv2.LINE_AA)
            print("verde")
            colorDetectado = True
            runScene("GREEN")
        # arduino.write(cad.encode('ascii'))
        elif color == (0, 0, 255):
            cv2.rectangle(frame, (x, y), (x+w, y+h), color, 3)
            cv2.putText(frame, 'Rojo', (x-10, y-10),
                        font, 0.75, color, 2, cv2.LINE_AA)
            print("rojo")
            colorDetectado = True
            cad = 'r'
            runScene("RED")
        # arduino.write(cad.encode('ascii'))
        else:
            print("No color")
            cad = '0'
        # arduino.write(cad.encode('ascii'))
    # return colorDetectado


Bajo, Alto = calcular_tres.valores('azul')
# azulBajo = np.array([100,100,20],np.uint8)
# azulAlto = np.array([125,255,255],np.uint8)
azulBajo = np.array(Bajo, np.uint8)
azulAlto = np.array(Alto, np.uint8)


Bajo, Alto = calcular_tres.valores('verde')
# amarilloBajo = np.array([15,100,20],np.uint8)
# amarilloAlto = np.array([45,255,255],np.uint8)

verdeBajo = np.array(Bajo, np.uint8)
verdeAlto = np.array(Alto, np.uint8)

Bajo, Alto = calcular_tres.valores('rojo')

rojoBajo = np.array(Bajo, np.uint8)
rojoAlto = np.array(Alto, np.uint8)
# redBajo1 = np.array([0,100,20],np.uint8)
# redAlto1 = np.array([5,255,255],np.uint8)
# redBajo2 = np.array([175,100,20],np.uint8)
# redAlto2 = np.array([179,255,255],np.uint8)


cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_SIMPLEX
c = 1
timeRate = 14  # interval of time (s) to capture frame

while True:

    ret, frame = cap.read()
    FPS = cap.get(5)

    if ret == True:

        frameRate = int(FPS) * timeRate
        if c%frameRate == 0:
            print("Comenzando a capturar frame")

            frameHSV = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
            maskAzul = cv2.inRange(frameHSV,azulBajo,azulAlto)
            maskVerde = cv2.inRange(frameHSV,verdeBajo,verdeAlto)
            maskRojo = cv2.inRange(frameHSV,rojoBajo,rojoAlto)

            cv2.imshow('frame',frame)

            try:
                dibujar(maskAzul,(255,0,0))
                dibujar(maskVerde,(0,255,0))
                dibujar(maskRojo,(0,0,255))
            except:
                print("Error!!!")
    
        c += 1
    
    if cv2.waitKey(1) & 0xFF == ord('s'):
      break
# arduino.close()
cap.release()
cv2.destroyAllWindows()