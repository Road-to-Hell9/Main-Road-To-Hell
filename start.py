from tkinter import *

start = Tk()
start.title("Main road to hell")
start['bg']='grey'

label_fenetre = Label(start,text="Menu",fg='white', bg="black",font="Arial 15 italic")
label_fenetre.pack()

bouton_jouer = Button(start,text = " Play ",bg='orange' )
bouton_jouer.pack(padx=5,pady=10)

player = IntVar()
nom = Entry(start, text="Your name", textvariable = player , width =10)
nom.pack(padx=5,pady=5)








start.mainloop()