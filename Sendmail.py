import smtplib
from tkinter import *
#
#
#
#
#
smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.ehlo()
smtpObj.starttls()
#
#
smtpObj.login('sergeymoroz0307@gmail.com' , '')     # PASSWORD HERE (Or from file)
#
# msg = input("Enter please your msg:\n")
fromadress = 'sergeymoroz0307@gmail.com'
# toadress = input("Enter please where you want to send: \n")
#
#
# try:
#     smtpObj.sendmail(fromadress, toadress, msg)
# except:
#     print("Ошибка")
# else:
#     print("Письмо пользователю" , toadress, "отправлено")
#     smtpObj.quit()

mGui = Tk()
mGui.geometry('550x600')
mGui.title("Отправить Email")

def button_clicked():
    print("Click")
    toadress = email_adress.get("1.0",END)
    msg = email_text.get("1.0", END)
    msg1 = msg.encode('cp1251')
    try:
        smtpObj.sendmail(fromadress, toadress, msg1)
    except (UnicodeEncodeError, smtplib.SMTPRecipientsRefused):
        result['text'] = 'Проверьте адрес, пожалуйста'
        result['bg'] = 'Crimson'
    else:
        result['text'] = 'Сообщение отправлено успешно!'
        result['bg'] = 'lawn green'
        email_text.delete(1.0, END)
    return toadress, msg

def ev(event):
    button = "Blue"

button = Button(mGui, bg = 'lightgray', text = 'Отправить письмо',command = button_clicked)
button.place(x = '350', y = '550')


email_text = Text(mGui, height = 22 , width = 45, font = 'times 12', wrap = WORD, relief = 'sunken')
email_text.place(x = '100', y = '70')

email_adress = Text(mGui, height = 1.45, width = 25, font = 'Arial 9')
email_adress.place(x = '285', y = '22')


email_id = Label(mGui, height = 2, width = 18, text = "Введите email адрес:")
email_id.place(x = '150', y = '15')

result = Label(mGui, height = 2, width = 40, font = 'Arial 12')
result.place(x = '99', y = '492')

mGui.mainloop()
