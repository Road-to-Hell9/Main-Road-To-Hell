from tkinter import *
from PIL import ImageTk, Image

##Start main game
def open_main():

    with open("Txt/scoreboard_name.txt" , "w" , encoding = "utf-8") as fichier :
        fichier.write(username.get())
    start.destroy()
    import Main

##canvas
start = Tk()
start.title("Main road to hell")
start['bg']='white'
start.geometry("1500x1000")
img = PhotoImage(file='Images/menubg.png')
label = Label(image=img)
label.place(x=0, y=0)

##score et player
username = StringVar()
nom = Entry(start, text="Your name", textvariable = username , width =10)
nom.pack(padx=5,pady=5)

label_fenetre = Label(start,text="Welcome",fg='black',font=("Times New Roman bold",70))
label_fenetre.pack()

bouton_jouer = Button(start,text = " wanna play? ",height = 5, width = 15,bg='green',fg='black', command = open_main)
bouton_jouer.pack(padx=10,pady=10)
bouton_quit=Button(start, text="Quit",height = 5, width = 15,bg='red',fg='white', command=start.destroy)
bouton_quit.pack(padx=1,pady=5)

start.mainloop()