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

def temp_text(e):
    nom.delete(0,"end")

##score et player
label_fenetre = Label(start,text="Welcome",fg='black',font=("Times New Roman bold",70))
label_fenetre.pack()
username = StringVar()
nom = Entry(start, textvariable = username , font=('Arial 24'))
nom.pack(padx=5,pady=5)

nom.insert(0, "Your name here......")
nom.bind("<FocusIn>", temp_text)

label_q = Label(start,text="Commands: Up=Q",fg='black',font=("Times New Roman bold",30))
label_q.pack()
label_s = Label(start,text="Middle=S",fg='black',font=("Times New Roman bold",30))
label_s.pack()
label_d = Label(start,text="Down=D",fg='black',font=("Times New Roman bold",30))
label_d.pack()

bouton_jouer = Button(start,text = " wanna play? ",height = 5, width = 15,bg='green',fg='black', command = open_main)
bouton_jouer.pack(padx=10,pady=10)
bouton_quit=Button(start, text="Quit",height = 5, width = 15,bg='red',fg='white', command=start.destroy)
bouton_quit.pack(padx=1,pady=5)

start.mainloop()