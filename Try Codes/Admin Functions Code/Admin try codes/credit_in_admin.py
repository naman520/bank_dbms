def credit_fun():
    import PySimpleGUI as sg
    import mysql.connector as sql

    # DB
    conn = sql.connect(host='localhost', user='root', passwd='123456', database='BANK_DBMS')
    cur = conn.cursor()
    # GUI
    sg.theme("LightBlue5")
    layout_1 = [[sg.Text('Account Number'), sg.InputText()],
              [sg.Button('Search'), sg.Button('Cancel')]]

    layout_2 = [[sg.Text('amount'), sg.InputText()],
               [sg.Button('Credit Amount'), sg.Button('Cancel')]]

    layout_3 = [[layout_1, sg.Column(layout_2, visible=False, key='-Col-')]]
    window = sg.Window('Admin', layout_3)

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
            try:
                print(values)

                get_money_query = "SELECT money FROM customer_login where acc_no = " + str(account_number)
                print(get_money_query)
                cur.execute(get_money_query)

                amount = cur.fetchall()[0][0]
                print(values)
                n = int(values[1])
                print(amount)
                money_query = "UPDATE customer_login SET money =" + str(amount + n) + " where acc_no = " + str(account_number)
                time_query = "UPDATE customer_login SET transaction_time = NOW() where acc_no = " + str(account_number)
                cur.execute(money_query)
                cur.execute(time_query)
                results = cur.fetchall()
                sg.popup("Transaction Success")
            except:
                sg.popup("Transaction Failed")

    conn.commit()
    window.close()

credit_fun()