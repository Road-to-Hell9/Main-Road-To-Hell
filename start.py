from tkinter import *
<<<<<<< Updated upstream
def open_main():
    start.destroy()
    import Main

=======
from Main import*
>>>>>>> Stashed changes
start = Tk()
start.title("Main road to hell")
start['bg']='grey'

label_fenetre = Label(start,text="Menu",fg='white', bg="black",font="Arial 15 italic")
label_fenetre.pack()

bouton_jouer = Button(start,text = " Play ",bg='orange', command = open_main )
bouton_jouer.pack(padx=5,pady=10)

player = IntVar()
nom = Entry(start, text="Your name", textvariable = player , width =10)
nom.pack(padx=5,pady=5)

win1 = Tk()
gui1 = Main.GUI(win1)
gui1.pack(fill="both", expand=True)

### the second GUI is in a Toplevel
##win2 = tk.Toplevel(win1)
##gui2 = GUI2.GUI(win2)
##gui2.pack(fill="both", expand=True)
##





start.mainloop()