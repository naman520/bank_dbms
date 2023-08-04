import PySimpleGUI as sg
import mysql.connector as sql

conn = sql.connect(host='localhost', user='root', passwd='123456', database='BANK_DBMS')
cur = conn.cursor()

sg.theme("LightBlue5")
layout = [[sg.Text('Account Number'),sg.InputText()],
        [sg.Button('Search'), sg.Button('Cancel')]]
layout2 = [ [sg.Text('amount'),sg.InputText()],
        [sg.Button('Credit Amount'), sg.Button('Cancel')]]

layout3 = [[layout,sg.Column(layout2,visible=False,key='-Col-')]]
window = sg.Window('Admin',layout3)
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
    if event == 'Credit Amount':
        if event == sg.WIN_CLOSED or event == 'Cancel':
            break
        #amount = values[3]
        try:
            money_query = "UPDATE customer_login SET money ="+ str(amount+results[0][3]) +" where acc_no = "+str(acc_no)
            time_query = "UPDATE customer_login SET transaction_time = NOW() where acc_no = "+str(acc_no)
            cur.execute(money_query)
            cur.execute(time_query)
            results = cur.fetchall()
            sg.popup("Transaction Success")
        except:
            sg.popup("Transaction Failed")
            
conn.commit()


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
