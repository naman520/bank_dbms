import PySimpleGUI as sg
import mysql.connector as sql

def amt():
    conn=sql.connect(host='localhost',user='root',passwd='123456',database='BANK_DBMS')
    cur = conn.cursor()
    amt = "SELECT money FROM customer_login"
    cur.execute(amt)
    results = cur.fetchall()

def credit(acc_no,name,amount):
    #database connection
    conn=sql.connect(host='localhost',user='root',passwd='123456',database='BANK_DBMS')
    cur = conn.cursor()
    query = "SELECT * FROM customer_login"
    cur.execute(query)
    results = cur.fetchall()

    #gui
    sg.theme('LightBlue5')
    layout = [  [sg.Text('Account Holder Name'),sg.InputText()],
                [sg.Text('Account Number'),sg.InputText()],
                [sg.Button('Search'), sg.Button('Cancel')] ]
    layout2 =[ [sg.Text('Amount to be Credited'),sg.InputText()],
                [sg.Button('Credit Amount'), sg.Button('Cancel Transaction')]]

# Create the Window
    window = sg.Window('Admin', layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
            break
        if (values[0] and values[1]) in results:
            window = sg.Window('Credit',layout2)
            while True:
                event, values = window.read()
                if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
                    break
                else:
                    


    window.close()

credit(1596,'john',2000)