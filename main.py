from tkinter import *
from tkinter import messagebox
import random

root = Tk()
root.geometry("500x600")

def age():
    if float(edtage.get()) >= 18:
        messagebox.showinfo("Message", "You meet the requirements")
    else:
        messagebox.showerror("Error", "You don't meet the requirements")


def lotto_num():
    lotto = list()
    for num in range(6):
        if num == 7:
            edtage.quit()
        else:
            lotto.append(edtage.get())
            edtage.insert(0, lotto)

root.mainloop()



