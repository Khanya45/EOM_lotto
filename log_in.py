from tkinter import *
from tkinter import messagebox
import random
from PIL import ImageTk, Image
# import main

root = Tk()
root.geometry("650x450")
root.title('LOGIN')
root.config(bg='#f48c06')

pic1 = Image.open("logo.png")
resize = pic1.resize((100, 60), Image.ANTIALIAS)
logo = ImageTk.PhotoImage(resize)
lbpic = Label(root, image=logo, bg='#f48c06')
lbpic.place(x=540, y=5)


pic = Image.open("welcome.png")
resized = pic.resize((260, 350), Image.ANTIALIAS)


lbTitle = Label(root, text='LOG IN', font='Times 30', bg='#f48c06')
lbTitle.place(x=380, y=40)

img = ImageTk.PhotoImage(resized)
lbpic = Label(root, image=img, bg='#f48c06')
lbpic.place(x=40, y=50)

lbPlayer = Label(root, text='Player ID', bg='#f48c06')
lbPlayer.place(x=330, y=120)
entyPlayer = Entry(root, width=30)
entyPlayer.place(x=330, y=145)


lbID = Label(root, text='ID Number', bg='#f48c06')
lbID.place(x=330, y=180)
entyID = Entry(root, width=30)
entyID.place(x=330, y=200)

btnEnter = Button(root, text='ENTER', width=20, borderwidth=3)
btnEnter.place(x=330, y=235)

btnExit = Button(root, text='EXIT', borderwidth=7)
btnExit.place(x=330, y=300)

root.mainloop()
