#Imports
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
##from keyboard import *

# Create object
root = Tk()

#Variables
xWmax = 870
yWmax = 570
Game = True
time_1 = 0
score = 0

xCsize = 2
yCsize = yWmax/2 - 117/2

#Imports
bg = PhotoImage(file = "pixel-street.png")
player_img = ImageTk.PhotoImage(file = "main-car.png")

#----------Code----------#
#timer
def Time():
    if Game == True:
        time_1 = time_1 + 1
        root.after(1000, Time)

root.geometry("870x570")

label1 = Label(root, image = bg)
label1.place(x = -2, y = -1)

player = Label(root, image = player_img, borderwidth=0)
player.place(x = xCsize, y = yCsize)

#Functions
def movement_down(event):
    player.place(x = xCsize, y = yCsize*2)
    print("s")
def movement_up(event):
    player.place(x = xCsize, y = yCsize/2)
    print("z")

root.bind("<z>",movement_up)
root.bind("<s>",movement_down)

#Game start
##while Game == True:
    #Keys

    #Hitboxes
        #Check player x and y
carXmin = player.winfo_rootx()
carYmin = player.winfo_rooty()
carXmax = player.winfo_rootx() + xCsize
carYmax = player.winfo_rooty() + yCsize
        #Check Red Car x and y
##movement und shit

# Execute tkinter
root.mainloop()