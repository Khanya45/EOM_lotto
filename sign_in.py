from tkinter import *
from tkinter import messagebox
import random
from PIL import ImageTk, Image
import main

root = Tk()
root.geometry("660x500")
root.title('SIGNIN')
root.config(bg='#f48c06')

pic1 = Image.open("logo.png")
resize = pic1.resize((100, 80), Image.ANTIALIAS)
logo = ImageTk.PhotoImage(resize)
lbpic = Label(root, image=logo, bg='#f48c06')
lbpic.place(x=550, y=5)

lbTitle = Label(root, text='SIGN IN', font='Times 30', bg='#f48c06')
lbTitle.place(x=380, y=40)

pic = Image.open("lotto.jpeg")
resized = pic.resize((260, 410), Image.ANTIALIAS)
img = ImageTk.PhotoImage(resized)
lbpic = Label(root, image=img, bg='#f48c06')
lbpic.place(x=40, y=50)

lbName = Label(root, text='Name', bg='#f48c06')
lbName.place(x=330, y=120)
entyName = Entry(root, width=30)
entyName.place(x=330, y=145)

lbEmail = Label(root, text='Email', bg='#f48c06')
lbEmail.place(x=330, y=180)
entyEmail = Entry(root, width=30)
entyEmail.place(x=330, y=200)

lbAddress = Label(root, text='Address', bg='#f48c06')
lbAddress.place(x=330, y=235)
entyAddress = Entry(root, width=30)
entyAddress.place(x=330, y=255)

lbID = Label(root, text='ID number', bg='#f48c06')
lbID.place(x=330, y=290)
entyID = Entry(root, width=30)
entyID.place(x=330, y=310)

btnEnter = Button(root, text='ENTER', width=20, borderwidth=3)
btnEnter.place(x=355, y=370)

btnEnter = Button(root, text='EXIT', borderwidth=5)
btnEnter.place(x=330, y=430)

root.mainloop()
