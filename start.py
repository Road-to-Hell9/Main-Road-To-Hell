from tkinter import *

root = Tk()
root.title("Main road to hell")
root['bg']='grey'

label_fenetre = Label(root,text="Menu",fg='white', bg="black",font="Arial 15 italic")
label_fenetre.pack()

bouton_jouer = Button(root,text = " Jouer ",bg='orange' )
bouton_jouer.pack(padx=5,pady=10)


player = IntVar()
nom = Entry(root, text="votre nom", textvariable = player , width =10)
nom.pack(padx=5,pady=5)








root.mainloop()