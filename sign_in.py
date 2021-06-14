from tkinter import *
from tkinter import messagebox
import random
from PIL import ImageTk, Image

root = Tk()
root.geometry("650x500")
root.title('SIGNIN')


pic = Image.open("lotto.jpeg")
resized = pic.resize((260, 410), Image.ANTIALIAS)

lbTitle = Label(root, text='SIGN IN', font='Times 30')
lbTitle.place(x=380, y=40)

img = ImageTk.PhotoImage(resized)
lbpic = Label(root, image=img)
lbpic.place(x=40, y=50)

lbName = Label(root, text='Name')
lbName.place(x=330, y=120)
entyName = Entry(root, width=30)
entyName.place(x=330, y=145)

lbEmail = Label(root, text='Email')
lbEmail.place(x=330, y=180)
entyEmail = Entry(root, width=30)
entyEmail.place(x=330, y=200)

lbAddress = Label(root, text='Address')
lbAddress.place(x=330, y=235)
entyAddress = Entry(root, width=30)
entyAddress.place(x=330, y=255)

lbID = Label(root, text='ID number')
lbID.place(x=330, y=290)
entyID = Entry(root, width=30)
entyID.place(x=330, y=310)

btnEnter = Button(root, text='ENTER', width=20, borderwidth=3)
btnEnter.place(x=355, y=370)

btnEnter = Button(root, text='EXIT', borderwidth=5)
btnEnter.place(x=500, y=430)

root.mainloop()
