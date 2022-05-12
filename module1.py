##def Time():
##    if Game == True:
##        time_1 = n + 1
##        root.after(1000, Time)
##def score():
##    while Game== True:
##        s=0
##        if time1//10==0:
##            n=n+1
##            print (s)
##

from tkinter import *
from Main import *
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