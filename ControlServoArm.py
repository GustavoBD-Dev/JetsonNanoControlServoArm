import time
import tkinter as tk
from tkinter import Button, ttk
from tkinter.constants import CENTER, END
from adafruit_servokit import ServoKit
import csv
kit = ServoKit(channels=16)
 
# store the position of servos, store 90° by default
positionServos = [90,90,90,90,90,90]

# stored positions of scenes, save list of list with angles each servo
storedPositions = []

# create the window 
MainWindow = tk.Tk()
MainWindow.title('Control Servo Arm')
MainWindow.geometry('800x550') 

# Agregamos la tabla
arbol = ttk.Treeview(MainWindow, 
    columns = (
        'Servo[0]',
        'Servo[1]',
        'Servo[2]',
        'Servo[3]',
        'Servo[4]',
        'Servo[5]'))

#encabezados de las columnas
arbol.heading('#0', text='LOOP')
arbol.heading('Servo[0]', text='Servo[0]')
arbol.heading('Servo[1]', text='Servo[1]')
arbol.heading('Servo[2]', text='Servo[2]')
arbol.heading('Servo[3]', text='Servo[3]')
arbol.heading('Servo[4]', text='Servo[4]')
arbol.heading('Servo[5]', text='Servo[5]')

# configuracion de las columnas
arbol.column("#0", width=70, anchor=CENTER)
arbol.column("Servo[0]", width=50, anchor=CENTER)
arbol.column("Servo[1]", width=50, anchor=CENTER)
arbol.column("Servo[2]", width=50, anchor=CENTER)
arbol.column("Servo[3]", width=50, anchor=CENTER)
arbol.column("Servo[4]", width=50, anchor=CENTER)
arbol.column("Servo[5]", width=50, anchor=CENTER)

# valores de la tabla
#arbol.insert("", END, text="1", values=('0', '50','120','59','90','90'))
#arbol.insert("", END, text="2", values=('0', '60','120','180','90','180'))

# posicion de la tabla 
arbol.place(x=400, y=10)
 
 
def print_selection_0(v):
    positionServos[0] = int(v)
    kit.servo[0].angle = int(v)

def print_selection_1(v):
    positionServos[1] = int(v)
    kit.servo[1].angle = int(v)

def print_selection_2(v):
    positionServos[2] = int(v)
    #n.config(text='you have selected ' + v)
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

# funcion que se ejecuta al presionar boton Grabar Posicion
def grabarPosicion():
    #print(arbol.get_children())
    #print(positionServos)
    arbol.insert("", END, 
        text="POS {}".format(len(arbol.get_children())), 
        values=( positionServos[0], positionServos[1],
            positionServos[2], positionServos[3],
            positionServos[4], positionServos[5]))

# funcion para eliminar posicion
def eliminarPosicion():
    posDelete = arbol.focus()
    if posDelete != '':
        #print("Elemento a eliminar ", posDelete)
        arbol.delete(posDelete)

# establece las posiciones que se han guardado
def ejecutarEscena():
    print("escena a ejecutar -> ", storedPositions)
    for i in range(len(storedPositions)):
        print("loop ejecutando escena")
        print(storedPositions[i][0], 
            storedPositions[i][1], 
            storedPositions[i][2],
            storedPositions[i][3],
            storedPositions[i][4],
            storedPositions[i][5])
        print("ejecutando escena")
        kit.servo[0].angle = int(storedPositions[i][0])
        kit.servo[1].angle = int(storedPositions[i][1])
        kit.servo[2].angle = int(storedPositions[i][2])
        kit.servo[3].angle = int(storedPositions[i][3])
        kit.servo[4].angle = int(storedPositions[i][4])
        kit.servo[5].angle = int(storedPositions[i][5])
        time.sleep(1)


def establecerEscena():
    # obtenemos el valor de las posiciones que se encuentran en la tabla
    data = arbol.get_children()
    for i in data:
        # return dictionary of data 
        dataSimple = arbol.item(i)
        # get list of position of servos and stored in list
        storedPositions.append(dataSimple['values'])
    # send to servos the angle of positions
    print("valores guardados -> ",storedPositions)

def guardarEscenaArchivo():
    with open('angleServosScene.csv', 'w',newline='') as file:
        writer = csv.writer(file)
        for i in storedPositions:
            writer.writerow(i)
        #writer.writerows(storedPositions)

def cargarEscenaArchivo():
    with open('angleServosScene.csv', 'r') as file:
        csv_reader = csv.reader(file, delimiter = ',')
        # Passing the cav_reader object to list() to get a list of lists
        list_of_rows = list(csv_reader)
        storedPositions = list_of_rows
    print(storedPositions)
    # establecemos los valore en la tabla
    for i in range(len(storedPositions)):
        arbol.insert("", END, 
        text="POS {}".format(len(arbol.get_children())), 
        values=( 
            storedPositions[i][0], 
            storedPositions[i][1],
            storedPositions[i][2], 
            storedPositions[i][3],
            storedPositions[i][4], 
            storedPositions[i][5]))

# BOTONES
botonGrabarPosicion = Button(MainWindow, 
    text="Grabar Posicion", 
    command=grabarPosicion).place(x=400, y=350)

botonEliminarPosicion = Button(MainWindow, 
    text="Eliminar Posicion", 
    command=eliminarPosicion).place(x=600, y=350)

botonEjecutarEscena = Button(MainWindow, 
    text="Ejecutar Escenas", 
    command=ejecutarEscena).place(x=600, y=500)
 
botonGuardarEsceneArchivo = Button(MainWindow,
    text="Guardar en Archivo",
    command=guardarEscenaArchivo).place(x=400, y=450)

botonCargarEsceneArchivo = Button(MainWindow,
    text="Cargar de Archivo",
    command=cargarEscenaArchivo).place(x=400, y=500)

botonEstablecerEscene = Button(MainWindow,
    text="Establecer Escena",
    command=establecerEscena).place(x=600, y=450)

MainWindow.mainloop()