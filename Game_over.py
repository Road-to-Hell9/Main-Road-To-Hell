from tkinter import *
from PIL import ImageTk, Image

##Read Files
hs = open("Txt/highscore.txt", "r")
highscore = int(hs.read())

us = open("Txt/scoreboard_name.txt", "r")
username = us.read()

sc = open("Txt/score.txt", "r")
score = int(sc.read())

#Window
end = Tk()
end.title("Main road to hell")
end['bg']='white'
end.geometry("1500x1000")

##Img
img = PhotoImage(file='Images/menubg.png')
label = Label(image=img)
label.place(x=0, y=0)

##text
label_fenetre = Label(end,text="GAME OVER",fg='red',font=("Times New Roman bold",150))
label_fenetre.pack()

##Close game or Restart
bouton_quit=Button(end, text="Quit",height = 5, width = 15,bg='red',fg='white', command=end.destroy)
bouton_quit.pack(padx=1,pady=5)

##Show score
    ##Check score and compare
if score < highscore:
    yourscore_show = Label(end,text= str(username)+ "'s score is:"+str(score),fg='black',font=("Times New Roman bold",50))
    yourscore_show.pack()

    highscore_show = Label(end,text="Current champion has "+str(highscore)+ " points",fg='black',font=("Times New Roman bold",25))
    highscore_show.pack()

elif score >= highscore:
    highscore = score

    yourscore_show = Label(end,text= str(username)+ " is the new chapion.\n His score is:"+str(score),fg='black',font=("Times New Roman bold",50))
    yourscore_show.pack()

    ##Update highscore file
    file = open("Txt/highscore.txt" , "w" , encoding = "utf-8")
    file.write(str(score))

end.mainloop()

