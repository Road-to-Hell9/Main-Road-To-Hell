from tkinter import *
from PIL import ImageTk, Image

yourscore = 666999
highscore = 1200000000000000000
champion = "ja "
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


yourscore_show = Label(end,text="your score is:"+str(yourscore),fg='black',font=("Times New Roman bold",50))
yourscore_show.pack()

highscore_show = Label(end,text="Current champion is "+str(champion)+ " with "+str(highscore)+ " points",fg='black',font=("Times New Roman bold",25))
highscore_show.pack()


##def show_score(x,y):
##    label_score = Label(text="Score:" + int(score), )
##    screen.blit(score, x,y)

##with open("scireboard.txt" , "w" , encoding = "utf-8") as fichier :
##    fichier.write(score)

##show_score(textX, textY)
end.mainloop()

