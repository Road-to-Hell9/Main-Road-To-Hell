#Imports
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

# Create object 
root = Tk()

#Variables


#Imports
bg = PhotoImage(file = "pixel-street.png")

#----------Code----------#
root.geometry("870x570")
# Show image using label
label1 = Label( root, image = bg)
label1.place(x = -2, y = -1)

# Execute tkinter
root.mainloop()