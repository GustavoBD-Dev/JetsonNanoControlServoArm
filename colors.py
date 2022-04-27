import cv2
import numpy as np
# captura de video 
cap = cv2.VideoCapture(0) 
while True:
     # Toma cada cuadro 
    _, frame = cap.read() 
    # Cambio de tamaño de la imagen 
    frame = cv2.resize(frame, (400, 300), interpolation= cv2.INTER_CUBIC)
    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # Definir rango de color en HSV
    lower_blue = np.array([100,50,50]) # valor minimo  
    upper_blue = np.array([130,255,255]) # valor maximo 
    # Umbral de la imagen HSV para obtener solo colores azules 
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    # Combinacion de imagen real con mascara filtrada
    res = cv2.bitwise_and(frame, frame, mask=mask)
    # Muestra imagen original 
    cv2.imshow('frame', frame)
    # Muestra mascara filtrada 
    cv2.imshow('mask', mask)
    # Muestra combinacion de imagen original con filtrada
    cv2.imshow('res', res)
    # Si se presiona [ESC] termina el programa 
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()