#Imports
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

# Create object
root = Tk()

#Variables
xWmax = 870
yWmax = 570

xplayer = 2
yplayer = yWmax/2 - 117/2

#Imports
bg = PhotoImage(file = "pixel-street.png")
player = PhotoImage(file = "main-car.png")
width, height = main-car.size
print(width, height)
#----------Code----------#
root.geometry("870x570")

label1 = Label(root, image = bg)
label1.place(x = -2, y = -1)

player = Label(root, image = player_img, borderwidth=0)
player.place(x = xplayer, y = yplayer)

carW = player.winfo_width()/2
carH = player.winfo_height()/2

# Execute tkinter
root.mainloop()