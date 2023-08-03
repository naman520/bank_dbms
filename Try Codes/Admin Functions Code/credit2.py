import PySimpleGUI as sg
import mysql.connector as sql

conn=sql.connect(host='localhost',user='root',passwd='123456',database='BANK_DBMS')
cur = conn.cursor()
query = "SELECT acc_no FROM customer_login"
cur.execute(query)
results = cur.fetchall()

sg.theme("LightBlue5")
layout = [[sg.Text('Account Number'),sg.InputText()],
        [sg.Button('Search'), sg.Button('Cancel')]]
layout2 = [ [sg.Text('Amount to be Credited'),sg.InputText()],
        [sg.Button('Credit Amount'), sg.Button('Cancel')]]

layout3 = [[layout,sg.Column(layout2,visible=False,key='-Col-')]]
window = sg.Window('Admin',layout3)
while True:
    event, values = window.read()
    values = tuple(values.values())
    values = values[0]
    print(values, results)
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    if event == 'search':
        account_number = values[0]
        if (account_number) in results:
            print("Account found:", account_number)
            window['-Col2-'].update(visible=True)
        else:
            print("Account not found:", account_number)
            sg.popup("Account not found. Please enter a valid account number.")

window.close()