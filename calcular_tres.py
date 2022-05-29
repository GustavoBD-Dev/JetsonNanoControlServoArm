import cv2
import numpy as np
import tomarFoto

def nothing(x):
    pass


# Load image
#tomarFoto


def valores(color): 
    valoresMax = []
    valoresMin = []
    
    image = cv2.imread('para_calcular_0.png')

# Create a window
    cv2.namedWindow(color)

# Create trackbars for color change
# Hue is from 0-179 for Opencv
    cv2.createTrackbar('HMin', color, 0, 179, nothing)
    cv2.createTrackbar('SMin', color, 0, 255, nothing)
    cv2.createTrackbar('VMin', color, 0, 255, nothing)

    cv2.createTrackbar('HMax', color, 0, 179, nothing)
    cv2.createTrackbar('SMax', color, 0, 255, nothing)
    cv2.createTrackbar('VMax', color, 0, 255, nothing)

    
        # Set default value for Max HSV trackbars
    cv2.setTrackbarPos('HMax', color, 179)
    cv2.setTrackbarPos('SMax', color, 255)
    cv2.setTrackbarPos('VMax', color, 255)


    # Initialize HSV min/max values
    hMin = sMin = vMin = hMax = sMax = vMax = 0
    phMin = psMin = pvMin = phMax = psMax = pvMax = 0
    while(1):
    # Get current positions of all trackbars
        hMin = cv2.getTrackbarPos('HMin', color)
        sMin = cv2.getTrackbarPos('SMin', color)
        vMin = cv2.getTrackbarPos('VMin', color)
        hMax = cv2.getTrackbarPos('HMax', color)
        sMax = cv2.getTrackbarPos('SMax', color)
        vMax = cv2.getTrackbarPos('VMax', color)

    # Set minimum and maximum HSV values to display
        lower = np.array([hMin, sMin, vMin])
        upper = np.array([hMax, sMax, vMax])

    # Convert to HSV format and color threshold
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, lower, upper)
        result = cv2.bitwise_and(image, image, mask=mask)

    # Print if there is a change in HSV value
        if((phMin != hMin) | (psMin != sMin) | (pvMin != vMin) | (phMax != hMax) | (psMax != sMax) | (pvMax != vMax) ):
            print("(hMin = %d , sMin = %d, vMin = %d), (hMax = %d , sMax = %d, vMax = %d)" % (hMin , sMin , vMin, hMax, sMax , vMax))
            phMin = hMin
            psMin = sMin
            pvMin = vMin
            phMax = hMax
            psMax = sMax
            pvMax = vMax
    
    
    # Display result image
        cv2.imshow('image', result)
        if cv2.waitKey(10) & 0xFF == ord('q'):
            valoresMin.append(hMin)
            valoresMin.append(sMin)
            valoresMin.append(vMin)
            valoresMax.append(hMax)
            valoresMax.append(sMax)
            valoresMax.append(vMax)
            break
    v1,v2 = valoresMin,valoresMax
    cv2.destroyAllWindows()
    return v1,v2

#a,b=valores()

#print(a)
#print(b)

