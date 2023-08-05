import PySimpleGUI as sg
import mysql.connector as sql
import credit_in_admin

conn=sql.connect(host='localhost',user='root',passwd='123456',database='BANK_DBMS')
cur = conn.cursor()
query = "SELECT * FROM admin"
cur.execute(query)
results = cur.fetchall()

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [[sg.Text('Username'),sg.InputText()],
            [sg.Text('Password'), sg.InputText(password_char='*')],
            [sg.Button('Login'), sg.Button('Cancel')]]
layout2 = [[sg.Button('Credit')]]
layout3 = [[layout, sg.Column(layout2, visible=False, key='-Col-')]]

# Create the Window
window = sg.Window('Window Title', layout3)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    if (values[0],values[1]) in results:
        print("Authentication successful")
        print("Authentication successful")
        window['-Col-'].update(visible=True)
        if event == 'credit':
            credit_in_admin.credit_fun()
    else:
        print("Authentication failed")
        event = sg.WIN_CLOSED
        break

window.close()