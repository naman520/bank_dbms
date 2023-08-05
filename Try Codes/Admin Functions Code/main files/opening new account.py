import PySimpleGUI as sg
import mysql.connector as sql
from datetime import datetime

conn = sql.connect(host='localhost', user='root', passwd='123456', database='BANK_DBMS')
cur = conn.cursor()

today = datetime.now()
formatted_date = today.strftime('%d-%m-%y %H:%M:%S')

sg.theme("SandyBeach")
layout = [[sg.Text('New Account Number'), sg.InputText(key='ACC')],
          [sg.Text('Name'),sg.InputText(key='Name')],
          [sg.Text('Login Pin'),sg.InputText(key='pin')],
          [sg.Text('Money'),sg.InputText(key='money')],
          [sg.Text('Time'),sg.Text(formatted_date)],
          [sg.Button('Create Account'), sg.Button('Cancel')]]

window = sg.Window('Account Creation', layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    if event == "Create Account":
            a = values['ACC']
            a2 = values['Name']
            a3 = values['pin']
            a4 = values['money']
            a6 = (a, a2, a3, a4)
            print(a6)

            query = "INSERT INTO customer_login (Name, acc_no, login_pin, money,transaction_time) VALUES (%s, %s, %s, %s,%s)"
            val = (a2, a, a3, a4,today)
            print(query,values)
            cur.execute(query,val)
            sg.popup("Account Created Successfully Account Number is",a,"in the name of",a2)
conn.commit()
window.close()