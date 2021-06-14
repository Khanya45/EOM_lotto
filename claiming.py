from tkinter import *
from tkinter import messagebox
import random

root = Tk()
root.geometry("450x500")
root.title('CLAIM PRIZE')

lbHeading = Label(root, text='Banking Details', font='Times 30')
lbHeading.place(x=80, y=40)

lbAccHolder = Label(root, text='Account Holder Name')
lbAccHolder.place(x=80, y=120)
entyAccHolder = Entry(root, width=30)
entyAccHolder.place(x=80, y=145)

lbAccNumber = Label(root, text='Account Number')
lbAccNumber.place(x=80, y=180)
entyAccNumber = Entry(root, width=30)
entyAccNumber.place(x=80, y=200)

lbBank = Label(root, text='Bank')
lbBank.place(x=80, y=235)
entyBank = Entry(root, width=30)
entyBank.place(x=80, y=255)

btnSubmit = Button(root, text='SUBMIT', width=20, borderwidth=3)
btnSubmit.place(x=80, y=300)

btnSubmit = Button(root, text='EXIT', borderwidth=7)
btnSubmit.place(x=80, y=390)

root.mainloop()
