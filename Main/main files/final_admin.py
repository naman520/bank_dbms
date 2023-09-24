import PySimpleGUI as sg
import mysql.connector as sql
import ona , credit2 , debit1

conn = sql.connect(host='localhost', user='root', passwd='123456', database='BANK_DBMS')
cur = conn.cursor()

def credit_window():
    credit2.creditt()

def debit_window():
    debit1.debitt()
def account():
    ona.new_account()

def main_window():
    query = "SELECT * FROM admin"
    cur.execute(query)
    results = cur.fetchall()

    sg.theme('DarkAmber')  # Add a touch of color
    # All the stuff inside your window.
    layout = [[sg.Image('Untitledlogo.png',expand_x=True, expand_y=True )],
            [sg.Text('Username'), sg.InputText()],
            [sg.Text('Password'), sg.InputText(password_char='*')],
            [sg.Button('Login'), sg.Button('Cancel')],
            [sg.Button('Credit')],[sg.Button('Debit')],[sg.Button('Account')]]

    # Create the Window
    window = sg.Window('Bank Admin GUI', layout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
            break
        if (values[1], values[2]) in results:
            print("Authentication successful")
            if event == 'Credit':
                credit_window()
            elif event == 'Debit':
                debit_window()
            elif event == 'Account':
                account()
        else:
            print("Authentication failed")
            sg.popup_auto_close('Wrong Id or Password \n please try again')
            event = sg.WIN_CLOSED
            break

    window.close()
