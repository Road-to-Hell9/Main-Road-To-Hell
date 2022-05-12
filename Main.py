#Imports
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
def movement():
    if keyboard.read_key()=="z":
        player.place(x = xCsize, y = yCsize*2)
    if keyboard.read_key()=="s":
        player.place(x = xCsize, y = yCsize/2)

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

#Game start
while Game == True:


    #Hitboxes
        #Check player x and y
    carXmin = player.winfo_rootx()
    carYmin = player.winfo_rooty()
    carXmax = player.winfo_rootx() + xCsize
    carYmax = player.winfo_rooty() + yCsize
        #Check Red Car x and y

# Execute tkinter
root.mainloop()