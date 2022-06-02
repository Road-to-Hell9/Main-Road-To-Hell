#Imports
from ast import Global
from time import time
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import random
# Create object
root = Tk()

#Variables
xWmax = 870
yWmax = 570
Game = False
time_1 = 0
score = 0
speed = 6

xCsize = 200
yCsize = yWmax/2 - 117/2
yNsize = yCsize
yNsize2 = yCsize
xNPC_1 = 1200
xNPC_ini = xNPC_1
xNPC_2 = 900
xNPC_ini2 = xNPC_2
xNPC_3 = 1200
random_pos = [yWmax - 160, 45, yCsize]

#Imports
bg = PhotoImage(file = "../Images/pixel-street.png")
player_img = ImageTk.PhotoImage(file = "../Images/main-car.png")
npc_img = ImageTk.PhotoImage(file = "../Images/red-car.png")

#----------Code----------#
root.geometry("870x570")

label1 = Label(root, image = bg)
label1.place(x = -2, y = -1)

player = Label(root, image = player_img, borderwidth=0)
player.place(x = 2, y = yCsize)

npc_1 = Label(root, image = npc_img, borderwidth=0)
npc_1.place(x = xNPC_1, y = yCsize)

npc_2 = Label(root, image = npc_img, borderwidth=0)
npc_2.place(x = xNPC_2, y = 45)

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

#Game start check true
def Main_game_start():
    global Game, time_1
    bouton_animer.pack_forget()
    if Game == False:
        Game = True
        Main_game()
        Time()
        Score()
    else:
        return("Already executed")

#timer
def Time():
    global time_1
    time_1 = time_1 + 1
    root.after(1000, Time)
    print(time_1)

#Score
def Score():
    global time_1, score, speed
    score = time_1*10
    root.after(2000, Score)
    label_score.config(text = score)
    print("your score is", score)

    if time_1 >= 20:
        speed = speed+(time_1/10)

#Main Game
def Main_game():
    global xNPC_1, xNPC_2, xCsize, root, Game, yNsize, speed, score
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

        #Pos
        xNPC_1 = xNPC_1 - speed
        npc_1.place(x = xNPC_1, y = yNsize)

        xNPC_2 = xNPC_2 - speed
        npc_2.place(x = xNPC_2, y = 45)

        #Check colision and stop game
    if carXmax >= npc1Xmin and carXmin <= npc1Xmax and carYmax >= npc1Ymin and carYmin <= npc1Ymax or carXmax >= npc2Xmin and carXmin <= npc2Xmax and carYmax >= npc2Ymin and carYmin <= npc2Ymax:
        Game = False
        root.destroy()
        import Game_over
        print("Game Over")
        #save score
        with open("../Txt/scoreboard.txt" , "w" , encoding = "utf-8") as fichier :
            fichier.write(score.get())

        #Check if NPC out of window
    if npc1Xmax < -5:
      yNsize = random.choice(random_pos)
      xNPC_1 = xNPC_ini
      print("car 1 pos", yNsize)
      npc_1.place(x = xNPC_1, y = yNsize)
    if npc2Xmax < -5:
      yNsize2 = random.choice(random_pos)
      xNPC_2 = xNPC_ini2
      print("car 2 pos", yNsize2)
      npc_2.place(x = xNPC_2, y = yNsize2)

        #Rep function
    if Game == True:
        root.after(50, Main_game)
    elif Game == False:
        print("")

# Execute tkinter
label_score = Label(root,text="0000",fg='black',font=("Times New Roman bold",30))
label_score.pack(side=TOP,anchor =NE)
bouton_animer = Button(root,bd=50,text = " Jouer ",bg='blue',command = Main_game_start)
bouton_animer.pack()
root.mainloop()