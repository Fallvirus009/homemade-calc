from tkinter import *
import math

pi = math.pi

def func1():
    hiddenBox.insert(END,'1')

    displayedBox.insert(END,'1')

def func2():
    hiddenBox.insert(END,'2')

    displayedBox.insert(END,'2')

def func3():
    hiddenBox.insert(END,'3')

    displayedBox.insert(END,'3')

def func4():
    hiddenBox.insert(END,'4')

    displayedBox.insert(END,'4')

def func5():
    hiddenBox.insert(END,'5')

    displayedBox.insert(END,'5')

def func6():
    hiddenBox.insert(END,'6')

    displayedBox.insert(END,'6')

def func7():
    hiddenBox.insert(END,'7')

    displayedBox.insert(END,'7')

def func8():
    hiddenBox.insert(END,'8')

    displayedBox.insert(END,'8')

def func9():
    hiddenBox.insert(END,'9')

    displayedBox.insert(END,'9')

def toPowerOf():
    hiddenBox.insert(END, " ** ")

    displayedBox.insert(END,' ^ ')

def func0():
    hiddenBox.insert(END,'0')

    displayedBox.insert(END,'0')

def funcDecimal():
    hiddenBox.insert(END, '.')

    displayedBox.insert(END,'.')

def funcDiv():
    hiddenBox.insert(END,' / ')

    displayedBox.insert(END,' / ')

def funcMult():
    hiddenBox.insert(END,' * ')

    displayedBox.insert(END,' * ')

def funcSub():
    hiddenBox.insert(END,' - ')

    displayedBox.insert(END,' - ')

def funcAdd():
    hiddenBox.insert(END,' + ')

    displayedBox.insert(END,' + ')

def funcClear():
    entry = hiddenBox.get()
    dispEntry = displayedBox.get()

    hiddenBox.delete(0,len(entry))
    displayedBox.delete(0,len(dispEntry))

def leftPar():
    hiddenBox.insert(END, " (")

    displayedBox.insert(END,' (')

def rightPar():
    hiddenBox.insert(END, ") ")

    displayedBox.insert(END,') ')

def funcSolve():
    expression = hiddenBox.get()

    hiddenBox.delete(0, len(expression))
    displayedBox.delete(0, len(expression))

    expression = eval(expression)

    displayedBox.insert(0, expression) 

def funcSqrt():
    hiddenBox.insert(END, " ** 0.5 ")

    displayedBox.insert(0,'\u221A')

def calcVolOfCylinder():
    cylinderHeight = cylinderHeightEntry.get()
    cylinderRadius = cylinderRadiusEntry.get()

    cylinderHeightEntry.delete(0, len(cylinderHeight))
    cylinderRadiusEntry.delete(0, len(cylinderRadius))

    cylinderHeight = float(cylinderHeight)
    cylinderRadius = float(cylinderRadius)

    cylinderVol = pi * (cylinderRadius ** 2) * cylinderHeight

    cylinderVolLabel.configure(text = str(cylinderVol), anchor = 'w')

def calcVolOfSphere():
    sphereRadius = sphereRadiusEntry.get()

    sphereRadiusEntry.delete(0, len(sphereRadius))

    sphereRadius = float(sphereRadius)

    sphereVol = (4/3) * pi * (sphereRadius ** 3)

    sphereVolLabel.configure(text = str(sphereVol), anchor = 'w')

def calculateVolOfCone():
    coneRadius = coneRadiusEntry.get()
    coneHeight = coneHeightEntry.get()

    coneRadiusEntry.delete(0, len(coneRadius))
    coneHeightEntry.delete(0, len(coneHeight))

    coneRadius = float(coneRadius)
    coneHeight = float(coneHeight)

    coneVol = pi * (coneRadius ** 2) * (coneHeight / 3)

    coneVolLabel.configure(text = str(coneVol), anchor = 'w')

def funcOff():
    quit(window)

def funcPi():
    hiddenBox.insert(END, math.pi)

    displayedBox.insert(END,'\u03C0')

window = Tk()
window.title("Calculator")

canvas = Canvas(window, width = 600, height = 525)
canvas.pack()

hiddenBox = Entry(window, font = "Verdana 40 bold", width = 10)
canvas.create_window(200, 55, window = hiddenBox)

displayedBox = Entry(window, font = "Verdana 40 bold", width = 10)
canvas.create_window(200, 55, window = displayedBox)

btn1 = Button(window, text = "1", width = 3, height = 1, font = "Verdana 20 bold", command = func1)
canvas.create_window(40, 200, window = btn1)

btn2 = Button(window, text = "2", width = 3, height = 1, font = "Verdana 20 bold", command = func2)
canvas.create_window(110, 200, window = btn2)

btn3 = Button(window, text = "3", width = 3, height = 1, font = "Verdana 20 bold", command = func3)
canvas.create_window(180, 200, window = btn3)

btn4 = Button(window, text = "4", width = 3, height = 1, font = "Verdana 20 bold", command = func4)
canvas.create_window(40, 260, window = btn4)

btn5 = Button(window, text = "5", width = 3, height = 1, font = "Verdana 20 bold", command = func5)
canvas.create_window(110, 260, window = btn5)

btn6 = Button(window, text = "6", width = 3, height = 1, font = "Verdana 20 bold", command = func6)
canvas.create_window(180, 260, window = btn6)

btn7 = Button(window, text = "7", width = 3, height = 1, font = "Verdana 20 bold", command = func7)
canvas.create_window(40, 320, window = btn7)

btn8 = Button(window, text = "8", width = 3, height = 1, font = "Verdana 20 bold", command = func8)
canvas.create_window(110, 320, window = btn8)

btn9 = Button(window, text = "9", width = 3, height = 1, font = "Verdana 20 bold", command = func9)
canvas.create_window(180, 320, window = btn9)

btn0 = Button(window, text = "0", width = 3, height = 1, font = "Verdana 20 bold", command = func0)
canvas.create_window(110, 380, window = btn0)

#Sqaure root
sqrtBtn = Button(window, text = "\u221A", width = 6, height = 1, font = "Verdana 20 bold", command = funcSqrt)
canvas.create_window(65, 130, window = sqrtBtn)

#Exponent
exponentBtn = Button(window, text = "^", width = 6, height =1, font = "Verdana 20 bold", command = toPowerOf)
canvas.create_window(200, 130, window = exponentBtn)

#Pi button
piBtn = Button(window, text = '\u03C0', width = 6, height =1, font = "Verdana 20 bold", command = funcPi)
canvas.create_window(335, 130, window = piBtn)

#Decimal point
decBtn = Button(window, text = ".", width = 3, height = 1, font = "Verdana 20 bold", command = funcDecimal)
canvas.create_window(180, 380, window = decBtn)

#Division sign
divBtn = Button(window, text = "/", width = 3, height = 1, font = "Verdana 20 bold", command = funcDiv)
canvas.create_window(250, 200, window = divBtn)

#Multiplication sign
multBtn = Button(window, text = "*", width = 3, height = 1, font = "Verdana 20 bold", command = funcMult)
canvas.create_window(250, 260, window = multBtn)

#Subtraction sign
subBtn = Button(window, text = "-", width = 3, height = 1, font = "Verdana 20 bold", command = funcSub)
canvas.create_window(250, 320, window = subBtn)

#Addition sign
addBtn = Button(window, text = "+", width = 3, height = 1, font = "Verdana 20 bold", command = funcAdd)
canvas.create_window(250, 380, window = addBtn)

#Clear button
clearBtn = Button(window, text = "C", width = 5, height = 1, font = "Verdana 20 bold", command = funcClear)
canvas.create_window(345, 200, window = clearBtn)

#Left parenthesis button
leftParBtn = Button(window, text = "(", width = 5, height = 1, font = "Verdana 20 bold", command = leftPar)
canvas.create_window(345, 260, window = leftParBtn)

#Right parenthesis button
rightParBtn = Button(window, text = ")", width = 5, height = 1, font = "Verdana 20 bold", command = rightPar)
canvas.create_window(345, 320, window = rightParBtn)

#Solve button
solveBtn = Button(window, text = "=", width = 5, height = 1, font = "Verdana 20 bold", command = funcSolve)
canvas.create_window(345, 380, window = solveBtn)

#Quit button
quitBtn = Button(window, text = "OFF", width = 3, height = 1, font = "Verdana 20 bold", command = funcOff)
canvas.create_window(40, 380, window = quitBtn)

#VOLUME SEGEMNT BEGINS -- VOLUME SEGEMNT BEGINS -- VOLUME SEGEMNT BEGINS -- VOLUME SEGEMNT BEGINS -- VOLUME SEGEMNT BEGINS -- VOLUME SEGEMNT BEGINS -- VOLUME SEGEMNT BEGINS

#Volume of sphere

sphereVolTypeLabel = Label(window, text = "Sphere Volume", font =  "Verdana 11 bold")
canvas.create_window(75, 430, window = sphereVolTypeLabel)

sphereVolBtn = Button(window, text = 'Calculate', font = "Verdana 10", width = 15, height = 1, command = calcVolOfSphere)
canvas.create_window(75, 455, window = sphereVolBtn)

sphereRadiusEntry = Entry(window, width = 9, font = "Verdana 13")
canvas.create_window(87, 485, window = sphereRadiusEntry)

sphereRadiusLabel = Label(window, text = "R", font = "Verdana 12 bold")
canvas.create_window(20, 485, window = sphereRadiusLabel)

sphereVolLabel = Label(window, text = "Volume", font = "Verdana 10 bold", width = 13)
canvas.create_window(75, 510, window = sphereVolLabel)

coneVolTypeLabel = Label(window, text = "Cone Volume", font =  "Verdana 11 bold")
canvas.create_window(200, 430, window = coneVolTypeLabel)

coneVolBtn = Button(window, text = 'Calculate', font = "Verdana 10", width = 12, height = 1, command = calculateVolOfCone)
canvas.create_window(200, 455, window = coneVolBtn)

coneHeightEntry = Entry(window, width = 3, font = "Verdana 12")
canvas.create_window(180, 485, window = coneHeightEntry)

coneHeightLabel = Label(window, text = "H", font =  "Verdana 10 bold")
canvas.create_window(153, 485, window = coneHeightLabel)

coneRadiusEntry = Entry(window, width = 3, font = "Verdana 12")
canvas.create_window(235, 485, window = coneRadiusEntry)

coneRadiusLabel = Label(window, text = "R", font =  "Verdana 10 bold")
canvas.create_window(207, 485, window = coneRadiusLabel)

coneVolLabel = Label(window, text = "Volume", font = "Verdana 10 bold", width = 11)
canvas.create_window(200, 510, window = coneVolLabel)

cylinderVolTypeLabel = Label(window, text = "Cylinder Volume", font =  "Verdana 11 bold")
canvas.create_window(330, 430, window = cylinderVolTypeLabel)

cylinderVolBtn = Button(window, text = 'Calculate', font = "Verdana 10", width = 16, height = 1, command = calcVolOfCylinder)
canvas.create_window(330, 455, window = cylinderVolBtn)

cylinderHeightLabel = Label(window, text = 'H', font =  "Verdana 11 bold")
canvas.create_window(270, 485, window = cylinderHeightLabel)

cylinderHeightEntry = Entry(window, font = "Verdana 12", width = 4)
canvas.create_window(305, 485, window = cylinderHeightEntry)

cylinderRadiusLabel = Label(window, text = 'R', font =  "Verdana 11 bold")
canvas.create_window(340, 485, window = cylinderRadiusLabel)

cylinderRadiusEntry = Entry(window, font = "Verdana 12", width = 4)
canvas.create_window(375, 485, window = cylinderRadiusEntry)

cylinderVolLabel = Label(window, text = "Volume", font = "Verdana 10 bold", width = 15)
canvas.create_window(330, 510, window = cylinderVolLabel)

window.mainloop()