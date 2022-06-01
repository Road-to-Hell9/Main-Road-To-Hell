from tkinter import *
from PIL import ImageTk, Image


def open_main():
    start.destroy()
    import Main

def valider():
    value=username.get()
    with open("fichier_1.txt" , "w" , encoding = "utf-8") as fichier :
        fichier.write(value)




##canvas
start = Tk()
start.title("Main road to hell")
start['bg']='white'
start.geometry("1500x1000")
img = PhotoImage(file='menubg.png')
label = Label(image=img)
label.place(x=0, y=0)

##score et player
username = str()
nom = Entry(start, text="Your name", textvariable = username , width =10)
nom.pack(padx=5,pady=5)



label_fenetre = Label(start,text="Welcome",fg='black',font=("Times New Roman bold",70))
label_fenetre.pack()



bouton_jouer = Button(start,text = " wanna play? ",height = 5, width = 15,bg='green',fg='black', command = open_main)
bouton_jouer.pack(padx=10,pady=10)
bouton_quit=Button(start, text="Quit",height = 5, width = 15,bg='red',fg='white', command=start.destroy)
bouton_quit.pack(padx=1,pady=5)

bouton_valider = Button(start,text = " sign me up ",bg='white',fg='black', command = valider)
with open("scoreboard.txt" , "r" , encoding = "utf-8") as fichier :
    for ligne in fichier :
        a=ligne
bouton_valider.pack(padx=0,pady=0)

start.mainloop()

