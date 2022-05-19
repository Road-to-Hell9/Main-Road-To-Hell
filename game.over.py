from tkinter import *
from PIL import ImageTk, Image


def close_main():
    end.destroy()
    import Main

end = Tk()
end.title("Main road to hell")
end['bg']='white'
end.geometry("1500x1000")


img = PhotoImage(file='menubg.png')
label = Label(image=img)
label.place(x=0, y=0)


label_fenetre = Label(end,text="GAME OVER",fg='red',font=("Times New Roman bold",150))
label_fenetre.pack()

bouton_jouer = Button(end,text = " try again? ",height = 5, width = 15,bg='green',fg='black', command = close_main )
bouton_jouer.pack(padx=10,pady=10)
bouton_quit=Button(end, text="Quit",height = 5, width = 15,bg='red',fg='white', command=end.destroy)
bouton_quit.pack(padx=1,pady=5)

player = IntVar()
nom = Entry(end, text="Your name", textvariable = player , width =10)
nom.pack(padx=5,pady=5)

end.mainloop()

