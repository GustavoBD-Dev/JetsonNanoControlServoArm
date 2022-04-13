import time
import tkinter as tk
from tkinter import Button, ttk
from tkinter.constants import CENTER, END
from adafruit_servokit import ServoKit
import csv
# object to contorl servos
kit = ServoKit(channels=16)
 
# store the position of servos, store 90° by default
positionServos = [90,90,90,90,90,90]

# stored positions of scenes, save list of list with angles each servo
storedPositions = []

# create the window 
MainWindow = tk.Tk()
MainWindow.title('Control Servo Arm')
MainWindow.geometry('800x550') 

# add table of scenes
tableScenes = ttk.Treeview(MainWindow, 
    columns = (
        'Servo[0]',
        'Servo[1]',
        'Servo[2]',
        'Servo[3]',
        'Servo[4]',
        'Servo[5]'))

# Head of columns
tableScenes.heading('#0', text='LOOP')
tableScenes.heading('Servo[0]', text='Servo[0]')
tableScenes.heading('Servo[1]', text='Servo[1]')
tableScenes.heading('Servo[2]', text='Servo[2]')
tableScenes.heading('Servo[3]', text='Servo[3]')
tableScenes.heading('Servo[4]', text='Servo[4]')
tableScenes.heading('Servo[5]', text='Servo[5]')

# setting of column
tableScenes.column("#0", width=70, anchor=CENTER)
tableScenes.column("Servo[0]", width=50, anchor=CENTER)
tableScenes.column("Servo[1]", width=50, anchor=CENTER)
tableScenes.column("Servo[2]", width=50, anchor=CENTER)
tableScenes.column("Servo[3]", width=50, anchor=CENTER)
tableScenes.column("Servo[4]", width=50, anchor=CENTER)
tableScenes.column("Servo[5]", width=50, anchor=CENTER)

# position of table 
tableScenes.place(x=400, y=10)
 
# funcitons to control of positions servos

def print_selection_0(v):
    positionServos[0] = int(v)
    kit.servo[0].angle = int(v)

def print_selection_1(v):
    positionServos[1] = int(v)
    kit.servo[1].angle = int(v)

def print_selection_2(v):
    positionServos[2] = int(v)
    kit.servo[2].angle = int(v)
     
def print_selection_3(v):
    positionServos[3] = int(v)
    kit.servo[3].angle = int(v)

def print_selection_4(v):
    positionServos[4] = int(v)
    kit.servo[4].angle = int(v)

def print_selection_5(v):
    positionServos[5] = int(v)
    kit.servo[5].angle = int(v)

# add sliders to control angle positions of servos 
# each slider set values of ona servo in the position of array

controlServo_0 = tk.Scale( MainWindow, label = 'Servo [0]', 
    from_ = 0, to = 180, orient = tk.HORIZONTAL, length = 300,
    showvalue = 90, tickinterval = 45, resolution = 1, 
    command = print_selection_0).place(x=10, y=10)

controlServo_1 = tk.Scale( MainWindow, label = 'Servo [1]', 
    from_ = 0, to = 180, orient = tk.HORIZONTAL, length = 300, 
    showvalue = 90, tickinterval = 45, resolution = 1,
    command = print_selection_1).place(x=10, y=90)

controlServo_2 = tk.Scale( MainWindow, label = 'Servo [2]', 
    from_ = 0, to = 180, orient = tk.HORIZONTAL, length = 300, 
    showvalue = 90, tickinterval = 45, resolution = 1,
    command = print_selection_2).place(x=10, y=170)

controlServo_3 = tk.Scale( MainWindow, label = 'Servo [3]', 
    from_ = 0, to = 180, orient = tk.HORIZONTAL, length = 300, 
    showvalue = 90, tickinterval = 45, resolution = 1,
    command = print_selection_3).place(x=10, y=250)

controlServo_4 = tk.Scale( MainWindow, label = 'Servo [4]', 
    from_ = 0, to = 180, orient = tk.HORIZONTAL, length = 300, 
    showvalue = 90, tickinterval = 45, resolution = 1,
    command = print_selection_4).place(x=10, y=330)

controlServo_5 = tk.Scale( MainWindow, label = 'Servo [5]', 
    from_ = 0, to = 180, orient = tk.HORIZONTAL, length = 300, 
    showvalue = 90, tickinterval = 45, resolution = 1,
    command = print_selection_5).place(x=10, y=410)

# functions of buttons
# Add the values of all sliders in the table 
def recordPosition():
    tableScenes.insert("", END, 
        text="POS {}".format(len(tableScenes.get_children())), 
        values=( positionServos[0], positionServos[1],
            positionServos[2], positionServos[3],
            positionServos[4], positionServos[5]))

# Delete the scene or positions of all servos that selected in table
def deletePosition():
    posDelete = tableScenes.focus()
    if posDelete != '':
        tableScenes.delete(posDelete)

# Send to servos all correspondind angles in each item of scene
def runScene():
    print("escena a ejecutar -> ", storedPositions)
    for i in range(len(storedPositions)):
        print("executing scene step : ",
            storedPositions[i][0], 
            storedPositions[i][1], 
            storedPositions[i][2],
            storedPositions[i][3],
            storedPositions[i][4],
            storedPositions[i][5])
        kit.servo[0].angle = int(storedPositions[i][0])
        kit.servo[1].angle = int(storedPositions[i][1])
        kit.servo[2].angle = int(storedPositions[i][2])
        kit.servo[3].angle = int(storedPositions[i][3])
        kit.servo[4].angle = int(storedPositions[i][4])
        kit.servo[5].angle = int(storedPositions[i][5])
        # delay betwen each step
        time.sleep(1)

def setScene():
    aux = []
    # get values of positions in table 
    data = tableScenes.get_children()
    for i in data:
        dataSimple = tableScenes.item(i) # return dictionary of data 
        # get list of position of servos and stored in list
        aux.append(dataSimple['values'])
    # set global variable the update scenes in aux
    global storedPositions 
    storedPositions = aux
    # send to servos the angle of positions
    print("Saved positions: ",storedPositions)

# save the array in the file csv
def saveSceneFile():
    with open('angleServosScene.csv', 'w',newline='') as file:
        writer = csv.writer(file)
        for i in storedPositions:
            writer.writerow(i)

# read and set values of file csv in table
def loadSceneFile():
    # if not data in tableScenes load the data of csv
    if tableScenes.get_children() == ():
        with open('angleServosScene.csv', 'r') as file:
            csv_reader = csv.reader(file, delimiter = ',')
            # Passing the cav_reader object to list() to get a list of lists
            list_of_rows = list(csv_reader)
            storedPositions = list_of_rows
        print(storedPositions)
        # set values in table
        for i in range(len(storedPositions)):
            tableScenes.insert("", END, 
            text="POS {}".format(len(tableScenes.get_children())), 
            values=( 
                storedPositions[i][0], 
                storedPositions[i][1],
                storedPositions[i][2], 
                storedPositions[i][3],
                storedPositions[i][4], 
                storedPositions[i][5]))

# Buttons
buttonRecordPosition = Button(MainWindow, 
    text="Grabar Posicion", 
    command=recordPosition).place(x=400, y=350)

buttonDeletePosition = Button(MainWindow, 
    text="Eliminar Posicion", 
    command=deletePosition).place(x=600, y=350)

buttonRunScene = Button(MainWindow, 
    text="Ejecutar Escenas", 
    command=runScene).place(x=600, y=500)
 
buttonSaveSceneFile = Button(MainWindow,
    text="Guardar en Archivo",
    command=saveSceneFile).place(x=400, y=450)

buttonLoadSceneFile = Button(MainWindow,
    text="Cargar de Archivo",
    command=loadSceneFile).place(x=400, y=500)

botonEstablecerEscene = Button(MainWindow,
    text="Establecer Escena",
    command=setScene).place(x=600, y=450)

# Run loop the window
MainWindow.mainloop()