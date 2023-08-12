import PySimpleGUI as sg
import mysql.connector as sql

conn=sql.connect(host='localhost',user='root',passwd='123456',database='BANK_DBMS')
cur = conn.cursor()


sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout1 = [[sg.Text('Username'),sg.InputText()],
            [sg.Text('Password'), sg.InputText(password_char='*')],
            [sg.Button('Login'), sg.Button('Cancel')]]
layout2 = [[sg.Button('Credit')]]
layout3 = [[sg.Text('Account Number'), sg.InputText()],
              [sg.Button('Search'), sg.Button('Cancel')]]

layout4 = [[sg.Text('amount'), sg.InputText()],
            [sg.Button('Credit Amount'), sg.Button('Cancel')]]

layout = [[layout1, layout2, sg.Column(layout3, visible=False, key='-Col1-'), sg.Column(layout4, visible=False, key='-Col2-')]]

# Create the Window
window = sg.Window('Window Title', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    query = "SELECT * FROM admin"
    cur.execute(query)
    results = cur.fetchall()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    if (values[0],values[1]) in results:
        print("Authentication successful")
        if event == 'Credit':
            window['-Col1-'].update(visible=True)
            print(values)
            if event == 'Search':
                account_number = values[2]
                print(values)
                try:
                    account_number = values[2]
                    q2 = "SELECT acc_no FROM customer_login where acc_no = " + str(account_number)
                    cur.execute(q2)
                    r2 = cur.fetchall()
                    print("Account found:", account_number)
                    window['-Col2-'].update(visible=True)
                except:
                    print("Account not found:", account_number)
                    sg.popup("Account not found. Please enter a valid account number.")

                if event == 'Credit Amount':
                    try:
                        print(values)
                        get_money_query = "SELECT money FROM customer_login where acc_no = " + str(account_number)
                        print(get_money_query)
                        cur.execute(get_money_query)
                        amount = cur.fetchall()[0][0]
                        n = int(values[3])
                        print(amount)
                        money_query = "UPDATE customer_login SET money =" + str(amount + n) + " where acc_no = " + str(account_number)
                        time_query = "UPDATE customer_login SET transaction_time = NOW() where acc_no = " + str(account_number)
                        cur.execute(money_query)
                        cur.execute(time_query)
                        r3 = cur.fetchall()
                        sg.popup("Transaction Success")
                    except:
                        sg.popup("Transaction Failed")

    else:
        print("Authentication failed")
        event = sg.WIN_CLOSED
        break

window.close()