import PySimpleGUI as sg
import mysql.connector as sql

conn = sql.connect(host='localhost', user='root', passwd='123456', database='BANK_DBMS')
cur = conn.cursor()

sg.theme("LightBlue5")
layout = [[sg.Text('Account Number'), sg.InputText()],
          [sg.Button('Search'), sg.Button('Cancel')]]
layout2 = [[sg.Text('Amount to be Credited'), sg.InputText()],
           [sg.Button('Credit Amount'), sg.Button('Cancel')]]

layout3 = [[layout, sg.Column(layout2, visible=False, key='-Col-')]]


def credit_window():
    window = sg.Window('Admin', layout3)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':
            break
        if event == 'Search':
            account_number = values[0]
            try:
                query = "SELECT acc_no FROM customer_login where acc_no = " + str(account_number)
                cur.execute(query)
                results = cur.fetchall()
                print("Account found:", account_number)
                window['-Col-'].update(visible=True)
            except:
                print("Account not found:", account_number)
                sg.popup("Account not found. Please enter a valid account number.")

    window.close()
