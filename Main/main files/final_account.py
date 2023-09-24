def customer():
    import PySimpleGUI as sg
    import mysql.connector as sql

    conn = sql.connect(host='localhost', user='root', passwd='123456', database='BANK_DBMS')
    cur = conn.cursor()

    query = "SELECT Name,acc_no,login_pin FROM customer_login"
    cur.execute(query)
    results = cur.fetchall()

    sg.theme('DarkAmber')  # Add a touch of color
    # All the stuff inside your window.
    layout = [[sg.Image('Untitledlogo.png',expand_x=True, expand_y=True )],
        [sg.Text('Account Holder Name',key = 'ACC'), sg.InputText()],
        [sg.Text('Account Number'), sg.InputText()],
        [sg.Text('Pin'), sg.InputText()],
        [sg.Button('Login'), sg.Button('Cancel'),sg.Button('Details')]]

    # Create the Window
    window = sg.Window('Customer GUI', layout,keep_on_top=True)
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
            if event == 'Details':
                account_number = values[1]
                q2 = "SELECT money FROM customer_login where acc_no =" + str(account_number)
                cur.execute(q2)
                r2 = cur.fetchall()
                sg.popup_scrolled("Account Holder Name --->"+str(values[0]),"\nAccount Number --->"+str(values[1]),"\nCurrent Account Balance--->"+str(r2),size=(300, 10))
            else:
                sg.popup_auto_close("Welcome")
        else:
            print("Authentication failed")
            event = sg.WIN_CLOSED
            break

    window.close()
