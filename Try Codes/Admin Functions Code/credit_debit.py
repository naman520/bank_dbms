import PySimpleGUI as sg
import mysql.connector as sql

conn=sql.connect(host='localhost',user='root',passwd='123456',database='BANK_DBMS')
cur = conn.cursor()

def amt():
    amt = "SELECT money FROM customer_login"
    cur.execute(amt)
    return 

def credit(acc_no,amount):
    #database connection
    
    query = "SELECT * FROM customer_login"
    cur.execute(query)
    results = cur.fetchall()

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
        if (values[1]) in results[1]:
            window = sg.Window('Credit',layout2)
            while True:
                event, values = window.read()
                if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
                    break
                else:
                    money_query = "UPDATE customer_login SET money ="+ str(amount+original) +" where acc_no = "+str(acc_no)

    window.close()

credit(1598,2000)