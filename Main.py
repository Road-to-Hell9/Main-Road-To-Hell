#Imports
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

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
xNPC_1 = 800

#Imports
bg = PhotoImage(file = "pixel-street.png")
player_img = ImageTk.PhotoImage(file = "main-car.png")
npc_img = ImageTk.PhotoImage(file = "red-car.png")

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

npc_1 = Label(root, image = npc_img, borderwidth=0)
npc_1.place(x = xNPC_1, y = yCsize)

#Keys
def movement_down(event):
    player.place(x = xCsize, y = yWmax - 160)
    print("d")
def movement_up(event):
    player.place(x = xCsize, y = 45)
    print("q")
def movement_mid(event):
    player.place(x = xCsize, y = yCsize)
    print("s")

root.bind("<q>",movement_up)
root.bind("<d>",movement_down)
root.bind("<s>",movement_mid)

#Game start
while Game == True:
    
# Execute tkinter
    root.mainloop()
#Pos
    xNPC_1 = xNPC_1 - 0.001
    print(xNPC_1)
    npc_1.place(relx = xNPC_1, rely = yCsize)
#Hitboxes
        #Check player x and y
    carXmin = player.winfo_rootx()
    carYmin = player.winfo_rooty()
    carXmax = player.winfo_rootx() + xCsize
    carYmax = player.winfo_rooty() + yCsize
        #Check Red Car x and y
    npcXmin = npc_1.winfo_rootx()
    npcYmin = npc_1.winfo_rooty()
    npcXmax = npc_1.winfo_rootx() + xCsize
    npcYmax = npc_1.winfo_rooty() + yCsize
        #Check colision
    #if carXmax >= npcXmin and carXmin <= npcXmax and carYmax >= npcYmin and carYmin <= npcYmax:
    #     Game = False
    #     print("Game Over")
    