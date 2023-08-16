import PySimpleGUI as sg
import mysql.connector as sql

conn = sql.connect(host='localhost', user='root', passwd='123456', database='BANK_DBMS')
cur = conn.cursor()

sg.theme('DarkAmber')

# Create a layout with a Text element to display account numbers
layout = [[sg.Text('Account Number'),sg.InputText()],
          [sg.Button('Search'),sg.Button('Exit')]]

window = sg.Window('Customer', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Search':
        account_number = values[0]
        try:
            query = f"SELECT * FROM customer_login where acc_no = '{account_number}'"
            cur.execute(query)
            result = cur.fetchone()
            if result:
                print("Account found:", account_number)
                sg.popup('Account found')
                q2 = "SELECT * FROM customer_login"
                sg.popup(result)
                print(q2)
            else:
                sg.popup('Error: Account Not Found')

        except sql.Error as e:
            print("Error:", e)
            sg.popup('Error: An error occurred')

conn.commit()
window.close()
