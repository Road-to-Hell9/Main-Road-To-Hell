# -*- coding: utf-8 *-*
#
# Exemple 2_25
# Déplacement au clavier
#

from tkinter import *
from PIL import Image, ImageTk

# fonction de déplacement

def Clavier(event):
    global X,Y
    touche = event.keysym
    # déplacement vers le haut
    if touche == 'Up':
        Y = Y - DEP
    # déplacement vers le bas
    if touche == 'Down':
        Y = Y + DEP
    # déplacement vers la droite
    if touche == 'Right':
        X = X + DEP
    # déplacement vers la gauche
    if touche == 'Left':
        X = X - DEP
    # on dessine le pion à sa nouvelle position
    Canevas.coords(vache_1,X , Y )

def Raz():
    Canevas.coords(vache_1,0,0)

def Valider():
    reponse_1=Choix_Final_1.get()
    reponse_2=Liste.get(Liste.curselection())
    print("Réponse 1 : ",reponse_1)
    print("Réponse 2 : ",reponse_2)

# Création de la fenêtre principale
fenetre = Tk()
fenetre.title("Déplacement clavier")

# Création d'un widget Canvas
mon_dossier = "Images\\"
DEP = 5
TAILLE = 10
X = 0
Y = 0
Canevas = Canvas(fenetre,width=500,height=500,bg ='cyan')

# Affichage Image png dans tkinter avec PIL
image_1 = ImageTk.PhotoImage(file=mon_dossier+"Vache.png")
vache_1 = Canevas.create_image(0,0,anchor=NW, image=image_1)

# On retaille à 100x100 Pixels
image_2 = Image.open(mon_dossier+"Vache.png").resize((100,100), Image.ANTIALIAS)
image_2 = ImageTk.PhotoImage(image_2)
vache_2 = Canevas.create_image(100,100,anchor=NW, image=image_2)

# On retaille avec un facteur d'échelle
image_3 = Image.open(mon_dossier+"Vache.png")
long,large=image_3.size
facteur=0.4
long=int(long*facteur)
large=int(large*facteur)
image_3 = image_3.resize((long, large), Image.ANTIALIAS)
image_3 = ImageTk.PhotoImage(image_3)
vache_3 = Canevas.create_image(200,200,anchor=NW, image=image_3)

# La méthode bind() permet de lier un événement avec une fonction
Canevas.focus_set()
Canevas.bind('<Key>',Clavier)

# Fenetre des réponses
frame_1 = Frame(fenetre,width=350,height=100,bg="grey",bd=4,relief=RAISED)
frame_1.pack(padx = 5,pady=5)

# Titre 1
label_1 = Label(frame_1,text="Autriche ",fg='blue', bg="yellow",font="Arial 15 italic")
label_1.grid(row=0,column=0,padx=10,pady=5)

# Type Bouton
# no_couleur.get() pour récupérer la valeur
Choix_Final_1 = IntVar()
choix_1 = Radiobutton (frame_1,text = " 1 ",variable = Choix_Final_1,value = 1)
choix_2 = Radiobutton (frame_1,text = " 2 ",variable = Choix_Final_1,value = 2)
choix_1.grid(row=0,column=1,padx=10,pady=5)
choix_2.grid(row=0,column=2,padx=10,pady=5)

# Titre 2
label_2 = Label(frame_1,text="Pays 1 ",fg='blue', bg="yellow",font="Arial 15 italic")
label_2.grid(row=1,column=0,padx=10,pady=5)

# Type Liste déroulante
Liste = Listbox(frame_1)
for pays in ["Autriche", "France", "Allemagne"]:
    Liste.insert(END, pays)
Liste.grid(row=1,column=1,padx=10,pady=5)

# Bouton de validation
Button(frame_1,text=' Valider' ,command=Valider).grid(row=2,column=1,padx=10,pady=5)

# Canevas
Canevas.pack(padx=10,pady=10,side=LEFT)
Button(fenetre,text=' Quitter' ,command=fenetre.destroy).pack(side=BOTTOM)
Button(fenetre,text=' RAZ' ,command=Raz).pack()

# Create a Tkinter variable
Choix = StringVar()

# Dictionary with options
Choix.set( 'Un Deux Trois')


fenetre.mainloop()