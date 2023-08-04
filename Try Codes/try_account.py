import PySimpleGUI as sg
import mysql.connector as sql

conn = sql.connect(host='localhost', user='root', passwd='123456', database='BANK_DBMS')
cur = conn.cursor()


def auth_user():
    query = "SELECT * FROM customer_login"
    cur.execute(query)
    results = cur.fetchall()

    sg.theme('DarkAmber')  # Add a touch of color
    # All the stuff inside your window.
    layout = [[sg.Text('Account Holder Name'), sg.InputText()],
              [sg.Text('Account Number'), sg.InputText()],
              [sg.Text('Pin'), sg.InputText()],
              [sg.Button('Login'), sg.Button('Cancel')]]

    # Create the Window
    window = sg.Window('Window Title', layout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        values = tuple(values.values())
        values = (values[0], int(values[1]), int(values[2]))
        print(values, results)
        if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
            break
        if (values[0], values[1], values[2]) in results:
            print("Authentication successful")
        else:
            print("Authentication failed")
            event = sg.WIN_CLOSED
            break

    window.close()
