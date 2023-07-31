import PySimpleGUI as sg
import mysql.connector as sql

conn=sql.connect(host='localhost',user='root',passwd='123456',database='BANK_DBMS')
cur = conn.cursor()

def amt():
    amt = "SELECT money FROM customer_login"
    cur.execute(amt)
    return 

def credit(acc_no,amount):
    #gui
    sg.theme('LightBlue5')
    layout = [  [sg.Text('Account Number'),sg.InputText()],
                [sg.Button('Search'), sg.Button('Cancel')] ]
    layout2 =[ [sg.Text('Amount to be Credited'),sg.InputText()],
                [sg.Button('Credit Amount'), sg.Button('Cancel Transaction')]]

# Create the Window
    window = sg.Window('Admin', layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
            break
        while True:
            event, values = window.read()

            query = "SELECT * FROM customer_login where acc_no = " + str(acc_no)
            cur.execute(query)
            results = cur.fetchall()

            print(values, results)

            if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
                break
            else:
                # money_query = "UPDATE customer_login SET money ="+ str(amount+results[3]) +" where acc_no = "+str(acc_no)
                break
    window.close()

credit(1598,2000)