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
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    if values in results:
        print("suceess")
        sg.Column(layout2,visible=True,key='-Col-')
    else:
        event = sg.WIN_CLOSED


window.close()