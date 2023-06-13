import PySimpleGUI as sg

def login_window():
    layout_admin = [
        [sg.Text('Admin Login')],
        [sg.Text('Username:'), sg.Input(key='-USERNAME-')],
        [sg.Text('Password:'), sg.Input(key='-PASSWORD-', password_char='*')],
        [sg.Button('Login'), sg.Button('Cancel')]
    ]

    return sg.Window('Login', layout_admin)

def customer():
    layout_customer = [
        [sg.Text("Account Holder")],
        [sg.Text('Account Number:'), sg.Input(key='-NUMBER-')],
        [sg.Text('OTP:'), sg.Input(key='-OTP-')],
        [sg.Button('Login'), sg.Button('Cancel')]
    ]

    return sg.Window('Login', layout_customer)

def main_window():
    layout = [
        [sg.Button('Admin'), sg.Button('Account Holder'), sg.Button('Exit')]
    ]

    return sg.Window('BANK DBMS', layout, finalize=True)

main = main_window()

while True:
    window,event, values = sg.read_all_windows()
    print(window,event, values)
    if event == sg.WINDOW_CLOSED or event == 'Exit':
        break

    if event == 'Admin':
        admin_window = login_window()

    if event == 'Account Holder':
        customer_window = customer()

    if event == 'Login':
        username = str(values['-USERNAME-'])
        password = str(values['-PASSWORD-'])
        
        # Add your authentication logic here
        if username == 'admin' and password == 'admin':
            sg.popup('Login Successful!')
        else:
            sg.popup('Invalid Credentials!')

        # Close the login window after login attempt
        admin_window.close()

    if event == 'Customer':
        number = values['-NUMBER-'] 
        otp = values['-OTP-']
        
        # Add your authentication logic here
        if number == 'admin' and otp == 'admin':
            sg.popup('Login Successful!')
        else:
            sg.popup('Invalid Credentials!')

        # Close the customer window after login attempt
        customer_window.close()

window.close()