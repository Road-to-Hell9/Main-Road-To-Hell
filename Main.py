#Imports
from tkinter import *
from tkinter import ttk
from start import *
from PIL import ImageTk, Image
<<<<<<< Updated upstream
from start import *
=======

>>>>>>> Stashed changes

# Create object
root = Tk()

#Variables
xWmax = 870
yWmax = 570
Game = True
time_1 = 0

xplayer = 2
yplayer = yWmax/2 - 117/2

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
player.place(x = xplayer, y = yplayer)

carW = player.winfo_width()/2
carH = player.winfo_height()


# Execute tkinter
root.mainloop()