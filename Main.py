#Imports
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

# Create object
root = Tk()

#Variables
xWmax = 870
yWmax = 570

carW = 75

xplayer = 2
yplayer = yWmax/2 - carW

#Imports
bg = PhotoImage(file = "pixel-street.png")
player = PhotoImage(file = "main-car.png")
width, height = main-car.size
print(width, height)
#----------Code----------#
root.geometry("870x570")

label1 = Label(root, image = bg)
label1.place(x = -2, y = -1)

lable2 = Label(root, image = player)
lable2.place(x = xplayer, y = yplayer)

# Execute tkinter
root.mainloop()