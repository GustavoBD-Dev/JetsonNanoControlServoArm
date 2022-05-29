#from ast import Try
import cv2
import numpy as np
import calcular_tres
import time
import asyncio

async def runScene(script):
  print("Ejecutando: ", script)
  await time.sleep(1)
  print("Fin de escena ", script)


def dibujar(mask,color):
  colorDetectado = False
  contornos,hierachy  = cv2.findContours(mask, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
  for c in contornos:
    area = cv2.contourArea(c)
    if area > 3000:
        x,y,w,h = cv2.boundingRect(c)
        if color == (255,0,0):
            cv2.rectangle(frame,(x,y),(x+w,y+h),color,3)
            cv2.putText(frame,'Azul',(x-10,y-10),font,0.75,color,2,cv2.LINE_AA)
            print("azul")
            colorDetectado = True
        #arduino.write(cad.encode('ascii'))
        elif color == (0,255,0):
            cv2.rectangle(frame,(x,y),(x+w,y+h),color,3)
            cv2.putText(frame,'Verde',(x-10,y-10),font,0.75,color,2,cv2.LINE_AA)
            print("verde")
            colorDetectado = True
        #arduino.write(cad.encode('ascii'))
        elif color == (0,0,255):
            cv2.rectangle(frame,(x,y),(x+w,y+h),color,3)
            cv2.putText(frame,'Rojo',(x-10,y-10),font,0.75,color,2,cv2.LINE_AA)
            print("rojo")
            colorDetectado = True
            cad = 'r'
        #arduino.write(cad.encode('ascii'))
        else:
            print("No color")
            cad = '0'
        #arduino.write(cad.encode('ascii'))
    #return colorDetectado



Bajo ,Alto = calcular_tres.valores('azul')      
#azulBajo = np.array([100,100,20],np.uint8)
#azulAlto = np.array([125,255,255],np.uint8)
azulBajo = np.array(Bajo,np.uint8)
azulAlto = np.array(Alto,np.uint8)


Bajo ,Alto = calcular_tres.valores('verde')      
#amarilloBajo = np.array([15,100,20],np.uint8)
#amarilloAlto = np.array([45,255,255],np.uint8)

verdeBajo = np.array(Bajo,np.uint8)
verdeAlto = np.array(Alto,np.uint8)

Bajo ,Alto = calcular_tres.valores('rojo') 

rojoBajo = np.array(Bajo,np.uint8)
rojoAlto = np.array(Alto,np.uint8)
#redBajo1 = np.array([0,100,20],np.uint8)
#redAlto1 = np.array([5,255,255],np.uint8)
#redBajo2 = np.array([175,100,20],np.uint8)
#redAlto2 = np.array([179,255,255],np.uint8)




cap = cv2.VideoCapture(1)

font = cv2.FONT_HERSHEY_SIMPLEX

while True:

  ret,frame = cap.read()

  if ret == True:
    frameHSV = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    maskAzul = cv2.inRange(frameHSV,azulBajo,azulAlto)
    maskVerde = cv2.inRange(frameHSV,verdeBajo,verdeAlto)
    maskRojo = cv2.inRange(frameHSV,rojoBajo,rojoAlto)
    

    try:
        """ if dibujar(maskAzul,(255,0,0)):
          asyncio.run(runScene("script to BLUE"))
        elif dibujar(maskVerde,(0,255,0)):
          asyncio.run(runScene("script to GREEN"))
        elif dibujar(maskRojo,(0,0,255)):
          asyncio.run(runScene("script to RED")) """
        dibujar(maskAzul,(255,0,0))
        dibujar(maskVerde,(0,255,0))
        dibujar(maskRojo,(0,0,255))
    except:

        print("No color!!!!!!!")
    
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('s'):
      break
#arduino.close()
cap.release()
cv2.destroyAllWindows()