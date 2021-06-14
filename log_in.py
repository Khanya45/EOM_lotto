from tkinter import *
from tkinter import messagebox
import random
from PIL import ImageTk, Image


root = Tk()
root.geometry("620x450")
root.title('LOGIN')


pic = Image.open("welcome.png")
resized = pic.resize((260, 350), Image.ANTIALIAS)

lbTitle = Label(root, text='LOG IN', font='Times 30')
lbTitle.place(x=380, y=40)

img = ImageTk.PhotoImage(resized)
lbpic = Label(root, image=img)
lbpic.place(x=40, y=50)

lbPlayer = Label(root, text='Player ID')
lbPlayer.place(x=330, y=120)
entyPlayer = Entry(root, width=30)
entyPlayer.place(x=330, y=145)

lbID = Label(root, text='ID Number')
lbID.place(x=330, y=180)
entyID = Entry(root, width=30)
entyID.place(x=330, y=200)

btnEnter = Button(root, text='ENTER', width=20, borderwidth=3)
btnEnter.place(x=330, y=235)

btnExit = Button(root, text='EXIT', borderwidth=7)
btnExit.place(x=330, y=300)

root.mainloop()
