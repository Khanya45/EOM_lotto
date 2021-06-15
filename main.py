import random
import datetime
import rsaidnumber
from tkinter import messagebox
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#  ------------------------- PLAY UNIT -----------------------------------------
def lottogenerator():
    lotto_prizes = {0: 0, 1: 0, 2: 20, 3: 100.50, 4: 2384, 5: 8584, 6: 10000000}
    count = 0
    userLotto = []
    winLotto = []
    for i in range(0, 6):
        rand_num = random.randint(1, 49)
        winLotto.append(rand_num)
        user_num = int(input("enter the lotto number"))
        userLotto.append(user_num)
    for i in range(0, 6):
        for y in range(0, 6):
            if userLotto[i] == winLotto[y]:
                count += 1
    prize = lotto_prizes[count]
    print(prize)


# lottogenerator()

#  ------------------------------ SIGN IN UNIT ------------------------------------
def age_validation():
    id = rsaidnumber.parse('0210160451089')
    birth_year = id.date_of_birth.year
    current_date = datetime.date.today()
    current_year = current_date.year
    age = current_year - birth_year
    if age >= 18:
        messagebox.showinfo("", "LETS PLAY")
    elif age < 18:
        messagebox.showinfo("", "You are too young to play")
    else:
        messagebox.showerror("", "Invalid ID number")


# age_validation()


def playerid_generator():
    first_5 = random.randint(10000, 99999)
    second_4 = random.randint(1000, 9999)
    third_3 = random.randint(100, 999)
    last_1 = random.randint(0, 9)
    print(first_5 + second_4 + third_3 + last_1)


# playerid_generator()

#  ----------- VALIDATION --------------
def email_validation(email):
    try:
        # if ("@" not in email) or ("." not in email):
        #     messagebox.showerror("", "Invalid email")
        # else:
        #     messagebox.showinfo("", "Valid email")
        sender_email_id = 'khanyagope93@gmail.com'
        receiver_email_id = email
        password = "GETRICHWITHLOTTO"
        subject = "Greetings"
        msg = MIMEMultipart()
        msg['From'] = sender_email_id
        msg['To'] = receiver_email_id
        msg['Subject'] = subject
        body = "hi guys how are you. i am doing fine\n"
        body = body + "How was your task yesterday"
        msg.attach(MIMEText(body, 'plain'))
        text = msg.as_string()
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(sender_email_id, password)
        s.sendmail(sender_email_id, receiver_email_id, text)
        s.quit()
    except ValueError:
        messagebox.showinfo("", "Valid email")


# email_validation("khanyagope93@gmail.com")


#  ----------------------------------- LOG IN UNIT -------------------------------------

#  ------ PLAYERID VALIDATION ---------
def playerid_validation(playerID):
    if playerID.isdigit() == False or len(playerID) != 13:
        messagebox.showerror("", "Invalid player ID")

#  ---------------------------------- CLAIM UNIT -----------------------------------

#  ----------- VALIDATION --------------
def validation(accNumber, accHolder, bank):
    if (accNumber.isdigit() == False) or (len(accNumber) < 9):
        messagebox.showerror("", "Invalid Account Number")
    elif (accHolder.isalpha() == False) or (accHolder == ""):
        messagebox.showerror("", "Invalid Account Holder")
    elif bank == "":
        messagebox.showerror("", "Choose the bank")
    else:
        messagebox.showinfo("", "You will hear from us within 10 minutes")



#  ---------- ID NUMBER VALIDATION --------

def id_validation():
    id_number = rsaidnumber.parse('0210160451089')
    if id_number.valid == False:
        messagebox.showerror("", "Invalid ID number")


# id_validation()

#  ------------------- FILE HANDLING --------------------

#  writing all the player's details and lotto results on a text file
def writeon_file(name, playerid, prize, sets, contacts, id):
    with open("playerDetails.txt", "w") as file:
        text = [name, playerid, sets, prize, contacts]
        file.writelines(text)


writeon_file("khanya", "8765675432123", "675", "45676545", "khanyagope93@gmail.com", "0210160451089")


def readfile(playerid, idnumber):
    with open("playerDetails.txt", "r") as file:
        for line in file:
            if (playerid in line) or (idnumber in line):
                messagebox.showinfo("", "Lets PLAY!!")
                break
            else:
                messagebox.showerror("", "Your account is not found")


readfile("87656732123", "0210160451089")
