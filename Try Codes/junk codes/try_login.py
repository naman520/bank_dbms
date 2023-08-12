import PySimpleGUI as sg
import mysql.connector as sql

conn=sql.connect(host='localhost',user='root',passwd='123456',database='BANK_DBMS')
cur = conn.cursor()
""" lid = "SELECT username FROM admin"
pas = "SELECT passwordx FROM admin" """
cur.execute("SELECT * FROM ADMIN")
results = cur.fetchall()
#conn.close()
#return results

uid = input("enter :")
pasw = input("enter :")

""" if uid == username:
    if pas != pasw:
        print("wrong")
elif uid != passwordx:
    print("wrong")
elif uid == lid:
    if pas == pasw:
        print("okkkk") """

if (uid, pasw) in results:
    print("Authentication successful")
else:
    print("Authentication failed")

conn.close()
""" def gui():
    admin_layout = [
                [sg.Text('Admin Login')],
                [sg.Text('Username: '), sg.Input(key='Username')],
                [sg.Text('Password: '), sg.Input(key='Password',password_char='*')],
                [sg.Button('Login'),sg.Button('Exit')]]

    layout = [[sg.Text('Welcome to STATE BANK OF INDIA'),sg.Column(admin_layout, visible=True)],
                [sg.Button('Admin'), sg.Button('Account'), sg.Button('Exit')]]

    window = sg.Window('Welcome to STATE BANK OF INDIA', layout)
    while True:
        event, values = window.read()
        print(event, values)
        if event in (None, 'Exit'):
            break
        if event == 'Admin':
            username = values['Username']
            password = values['Password']
            login_success = False

            #results = database()
            for row in lid:
                if row[0] == username:
                    login_success = True
                    break

            if login_success:
                sg.popup('Login Successful!')
            else:
                sg.popup_error('Invalid Credentials!', title='Error')

    window.close()


gui() """