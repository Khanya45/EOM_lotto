from tkinter import *
from tkinter import messagebox
import random
from PIL import ImageTk, Image
import main

root = Tk()
root.geometry("455x520")
root.title('PLAY')
root.config(bg='#f48c06')

pic1 = Image.open("logo.png")
resize = pic1.resize((100, 60), Image.ANTIALIAS)
logo = ImageTk.PhotoImage(resize)
lbpic = Label(root, image=logo, bg='#f48c06')
lbpic.place(x=350, y=5)


lbUser_lotto_num = Label(root, text='User Lottery Number:', bg='#f48c06')
lbUser_lotto_num.place(x=50, y=40)

# six entries to enter lottery numbers
entyUser_1 = Entry(root, width=5)
entyUser_1.place(x=50, y=70)
entyUser_2 = Entry(root, width=5)
entyUser_2.place(x=100, y=70)
entyUser_3 = Entry(root, width=5)
entyUser_3.place(x=150, y=70)
entyUser_4 = Entry(root, width=5)
entyUser_4.place(x=200, y=70)
entyUser_5 = Entry(root, width=5)
entyUser_5.place(x=250, y=70)
entyUser_6 = Entry(root, width=5)
entyUser_6.place(x=300, y=70)

lbUser_lotto_num = Label(root, text='Winning Lottery Number:', bg='#f48c06')
lbUser_lotto_num.place(x=50, y=150)

# six entries for winning lottery numbers
entyWin_1 = Entry(root, width=5)
entyWin_1.place(x=50, y=180)
entyWin_2 = Entry(root, width=5)
entyWin_2.place(x=100, y=180)
entyWin_3 = Entry(root, width=5)
entyWin_3.place(x=150, y=180)
entyWin_4 = Entry(root, width=5)
entyWin_4.place(x=200, y=180)
entyWin_5 = Entry(root, width=5)
entyWin_5.place(x=250, y=180)
entyWin_6 = Entry(root, width=5)
entyWin_6.place(x=300, y=180)

lbUser_lotto_num = Label(root, text='Number of matches:', bg='#f48c06')
lbUser_lotto_num.place(x=50, y=260)

#  An entry for number of matches
entyMatches = Entry(root, width=7)
entyMatches.place(x=50, y=290)

lbUser_lotto_num = Label(root, text='Prize:', bg='#f48c06')
lbUser_lotto_num.place(x=250, y=260)

#  An entry for number of matches
entyMatches = Entry(root, width=10)
entyMatches.place(x=250, y=290)

#  button for lottery generator
btnPlay = Button(root, text='PLAY', width=10, borderwidth=3)
btnPlay.place(x=70, y=390)

#  button for playing again/clearing the entries
btnReset = Button(root, text='RESET', width=10, borderwidth=3)
btnReset.place(x=200, y=390)

# This button is going to display when the entry of the prize is greater than 0
btnReset = Button(root, text='CLAIM', width=10, borderwidth=3)
btnReset.place(x=200, y=390)

#  button for exiting
btnExit = Button(root, text='EXIT', font='bold', borderwidth=7)
btnExit.place(x=150, y=470)



root.mainloop()
