#Imports
from ast import Global
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

xCsize = 200
yCsize = yWmax/2 - 117/2
xNPC_1 = 1200
xNPC_2 = 1200
xNPC_3 = 1200

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
player.place(x = 2, y = yCsize)

npc_1 = Label(root, image = npc_img, borderwidth=0)
npc_1.place(x = xNPC_1, y = yCsize)

npc_2 = Label(root, image = npc_img, borderwidth=0)
npc_2.place(x = xNPC_2, y = 45)

npc_3 = Label(root, image = npc_img, borderwidth=0)
npc_3.place(x = xNPC_3, y = yWmax - 160)

#Keys
def movement_down(event):
    player.place(x = 2, y = yWmax - 160)
    print("d")
def movement_up(event):
    player.place(x = 2, y = 45)
    print("q")
def movement_mid(event):
    player.place(x = 2, y = yCsize)
    print("s")

root.bind("<q>",movement_up)
root.bind("<d>",movement_down)
root.bind("<s>",movement_mid)

def main_game():
    global xNPC_1, xNPC_2, xNPC_3, xCsize, root, Game
#Game start
    if Game == True:
#Hitboxes
        #Check player x and y
        carXmin = player.winfo_rootx()
        carYmin = player.winfo_rooty()
        carXmax = player.winfo_rootx() + xCsize
        carYmax = player.winfo_rooty() + 117
        #Check Red Car x and y
        npc1Xmin = npc_1.winfo_rootx()
        npc1Ymin = npc_1.winfo_rooty()
        npc1Xmax = npc_1.winfo_rootx() + xCsize
        npc1Ymax = npc_1.winfo_rooty() + 117
        
        npc2Xmin = npc_2.winfo_rootx()
        npc2Ymin = npc_2.winfo_rooty()
        npc2Xmax = npc_2.winfo_rootx() + xCsize
        npc2Ymax = npc_2.winfo_rooty() + 117
        
        npc3Xmin = npc_3.winfo_rootx()
        npc3Ymin = npc_3.winfo_rooty()
        npc3Xmax = npc_3.winfo_rootx() + xCsize
        npc3Ymax = npc_3.winfo_rooty() + 117
        #Pos
        xNPC_1 = xNPC_1 - 3
        npc_1.place(x = xNPC_1, y = yCsize)
        
        xNPC_2 = xNPC_2 - 3
        npc_2.place(x = xNPC_2, y = 45)

        #Check colision
    if carXmax >= npc1Xmin and carXmin <= npc1Xmax and carYmax >= npc1Ymin and carYmin <= npc1Ymax or carXmax >= npc2Xmin and carXmin <= npc2Xmax and carYmax >= npc2Ymin and carYmin <= npc2Ymax or carXmax >= npc3Xmin and carXmin <= npc3Xmax and carYmax >= npc3Ymin and carYmin <= npc3Ymax:
        Game = False
        print("Game Over")
        
    if Game == True:
        root.after(50, main_game)
    elif Game == False:
        print("")
    
    # Execute tkinter
bouton_animer = Button(root,bd=5,text = " Jouer ",bg='blue',command = main_game)
bouton_animer.pack(side=TOP,padx=10,pady=10)
root.mainloop()