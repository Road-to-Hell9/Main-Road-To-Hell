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
<<<<<<< HEAD
bg = PhotoImage(file = "pixel-street.png")
player = PhotoImage(file = "main-car.png")
width, height = main-car.size
print(width, height)
=======
bg = PhotoImage(file = "pixel-street.png") 
player = ImageTk.PhotoImage(file = "main-car.png")

>>>>>>> c64cbe6cb8d12e6253076e8510f501b65e1213be
#----------Code----------#
root.geometry("870x570")

label1 = Label(root, image = bg)
label1.place(x = -2, y = -1)

lable2 = Label(root, image = player, borderwidth=0)
lable2.place(x = xplayer, y = yplayer)

# Execute tkinter
root.mainloop()