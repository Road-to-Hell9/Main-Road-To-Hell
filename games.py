from tkinter import *
from tkinter import ttk
from tkvideo import tkvideo
from PIL import ImageTk, Image
##sprites

class GFG:
    def __init__(self, master = None):
        self.master = master
        self.x = 1
        self.y = 0
        self.canvas = Canvas(my_label, width=1080, height=720, bg="yellow")


##        self.rectangle = self.canvas.create_image(400,600, image = sprite1, anchor = NE)
        self.rectangle = self.canvas.create_rectangle(20,20,60,60, fill="green", tags=("green",))
        self.canvas.pack()
        self.movement()

    def movement(self):


        self.canvas.move(self.rectangle, self.x, self.y)

        self.canvas.after(100, self.movement)

    # for motion in negative x direction
    def left(self, event):
        print(event.keysym)
        self.x = -20
        self.y = 0

    # for motion in positive x direction
    def right(self, event):
        print(event.keysym)
        self.x = 20
        self.y = 0

    # for motion in positive y direction
    def up(self, event):
        print(event.keysym)
        self.x = 0
        self.y = -5

    # for motion in negative y direction
    def down(self, event):
        print(event.keysym)
        self.x = 0
        self.y = 5



root = Tk()

sprite1 = PhotoImage(file = r'C:\Users\admin\Desktop\project\guideo\carsprite.png')
sprite1 = sprite1.subsample(3,3)
##window parameters
root.geometry("1280x720")
root.title('Highway to Hell')
root.wm_attributes("-transparentcolor", "yellow")
##video
my_label = Label(root)
my_label.pack()
my_label1 = Label(root)
my_label1.pack()

player = tkvideo(r"C:\Users\admin\Desktop\project\guideo\video.mp4", my_label1, loop = 1, size = (1280,720))
player.play()


##interractable
button = Button(root, text='Play', width=25,)
button.pack()
##class and object
gfg = GFG(root)
root.bind("<KeyPress-Right>", lambda e: gfg.right(e))
root.bind("<KeyPress-Left>", lambda e: gfg.left(e))









root.mainloop()
