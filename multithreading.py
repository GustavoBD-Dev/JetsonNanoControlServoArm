import threading
import time

positionServos = [90,90,90,90,90,90]
timeControl = 0.05


def moveServo(servo, actualPosition, newAnglePosition):
    #print("Hola Mundo " + str(servo) + " " + str(actualPosition) + " " + str(newAnglePosition))
    if newAnglePosition < actualPosition:
        for i in range(actualPosition, newAnglePosition - 1, -1):
            # set pos servo increment, set value i
            # print(servo, ' ', i)
            positionServos[servo] = i
            time.sleep(timeControl) # time in seconds
    elif newAnglePosition > actualPosition:
        for i in range(actualPosition, newAnglePosition + 1, 1):
            # set pos servo decrement, set value i
            # print(servo, ' ', i)
            positionServos[servo] = i
            time.sleep(timeControl) # time in seconds
    else:
        print('NO MOVE SERVO')
    print(positionServos)


def getExecuteData():
    import csv
    storedPositions = []
    with open('angleServosScene.csv', 'r') as file:
        csv_reader = csv.reader(file, delimiter = ',')
        list_of_rows = list(csv_reader)
        storedPositions = list_of_rows
    print(storedPositions)
    return storedPositions




if __name__ == "__main__":

    # Get data of file csv
    storedPositions = getExecuteData()

    print(positionServos)
    threadServos = []
    # thread aux variable
    thread = None

    for i in range(6):
        thread = threading.Thread(
                        target = moveServo, 
                        args = (i, 90, 120,))
        threadServos.append(thread) 

    for i in range(6):
       threadServos[i].start()


