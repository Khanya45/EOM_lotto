from tkinter import *
from tkinter import messagebox
import random
from PIL import ImageTk, Image
from tkinter import ttk
import main

root = Tk()
root.geometry("460x500")
root.title('CLAIM PRIZE')
root.config(bg='#f48c06')

pic1 = Image.open("logo.png")
resize = pic1.resize((100, 80), Image.ANTIALIAS)
logo = ImageTk.PhotoImage(resize)
lbpic = Label(root, image=logo, bg='#f48c06')
lbpic.place(x=350, y=5)

lbHeading = Label(root, text='Banking Details', font='Times 30', bg='#f48c06')
lbHeading.place(x=80, y=40)

lbAccHolder = Label(root, text='Account Holder Name', bg='#f48c06')
lbAccHolder.place(x=80, y=120)
entyAccHolder = Entry(root, width=30)
entyAccHolder.place(x=80, y=145)

lbAccNumber = Label(root, text='Account Number', bg='#f48c06')
lbAccNumber.place(x=80, y=180)
entyAccNumber = Entry(root, width=30)
entyAccNumber.place(x=80, y=200)

lbBank = Label(root, text='Bank', bg='#f48c06')
lbBank.place(x=80, y=235)
cbBank = ttk.Combobox(root)
cbBank['values'] = ["ABSA", "CAPITEC", "FNB", "STANDARD BANK"]
cbBank.place(x=80, y=255)


btnSubmit = Button(root, text='SUBMIT', width=20, borderwidth=3)
btnSubmit.place(x=80, y=300)

btnSubmit = Button(root, text='EXIT', borderwidth=7)
btnSubmit.place(x=80, y=390)

root.mainloop()
