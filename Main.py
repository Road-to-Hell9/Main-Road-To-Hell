#Imports
from tkinter import *
from tkinter import ttk
from tkinter.constants import *
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
player_img = ImageTk.PhotoImage(file = "main-car.png")

#----------Code----------#
root.geometry("870x570")

label1 = Label(root, image = bg)
label1.place(x = -2, y = -1)

player = Canvas(root, width=10, height=10)
player.pack
player.create_image(xplayer, yplayer, anchor=NW, image = player_img)

# Execute tkinter
root.mainloop()