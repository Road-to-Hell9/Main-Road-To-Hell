from tkinter import *
from PIL import ImageTk, Image


def open_main():
    start.destroy()
    import Main

start = Tk()
start.title("Main road to hell")
start['bg']='white'
start.geometry("1500x1000")


img = PhotoImage(file='menubg.png')
label = Label(image=img)
label.place(x=0, y=0)


label_fenetre = Label(start,text="Welcome",fg='black',font=("Times New Roman bold",70))
label_fenetre.pack()

bouton_jouer = Button(start,text = " wanna play? ",height = 5, width = 15,bg='green',fg='black', command = open_main )
bouton_jouer.pack(padx=10,pady=10)
bouton_quit=Button(start, text="Quit",height = 5, width = 15,bg='red',fg='white', command=start.destroy)
bouton_quit.pack(padx=1,pady=5)

player = IntVar()
nom = Entry(start, text="Your name", textvariable = player , width =10)
nom.pack(padx=5,pady=5)

start.mainloop()

