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
            [sg.Text('Account Number:'),sg.Input(key='-NUMBER-')],
            [sg.Text('OTP:'),sg.Input(key='-OTP-')],
            [sg.Button('Login'), sg.Button('Cancel')]
        ]

    return sg.Window('Login', layout_customer)
""" layout = [[sg.Column(layout_admin, key='ADMIN'), sg.Column(layout_customer, visible=False, key='ACCOUNT HOLDER')],
[sg.Button('try button'), sg.Button('1'), sg.Button('2'), sg.Button('3'), sg.Button('Exit')]]
"""
layout = [sg.Button('Admin'),sg.Button('Account Holder'),sg.Button('Exit')]

window = sg.Window('Swapping the contents of a window', layout)

layout =1

while True:
    event, values = sg.read_all_windows()
    print(event, values)
    # ADMIN LOGIN CODE
    if window == window and event == sg.WINDOW_CLOSED:
        break

    if window == window and event == 'ADMIN':
        if event == 'ADMIN':
            login_window = login_window()

    if event == sg.WINDOW_CLOSED or event == 'Exit':
        login_window.close()

    if event == 'Admin' and event == 'Login':
        username = str(values['-USERNAME-'])
        password = str(values['-PASSWORD-'])
        
        # Add your authentication logic here
        if username == 'admin' and password == 'admin':
            sg.popup('Login Successful!')
        else:
            sg.popup('Invalid Credentials!')

        # Close the login window after login attempt
        login_window.close()

    #Customer Login code
    if window == window and event == sg.WINDOW_CLOSED:
        break

    if window == window and event == 'Account Holder':
        if event == 'Account Holder':
            customer = customer()

    if event == sg.WINDOW_CLOSED or event == 'CanceExit':
        customer.close()

    if event == 'Customer' and event == 'Login':
        number = values['-NUMBER-'] 
        otp = values['-OTP-']
        
        # Add your authentication logic here
        if number == 'admin' and otp == 'admin':
            sg.popup('Login Successful!')
        else:
            sg.popup('Invalid Credentials!')

        # Close the login window after login attempt
        customer.close()



""" while True:
    event, values = window.read()
    print(event, values)
    if event in (None, 'Exit'):
        break
    if event == 'Admin':
        login_window = login_window()
        number = values['-NUMBER-'] 
        otp = values['-OTP-']
    if event == 'Account Holder':
        customer = customer()
        number = values['-NUMBER-'] 
        otp = values['-OTP-'] """
"""window[f'-COL{layout}-'].update(visible=False)
layout = int(event)
window[f'-COL{layout}-'].update(visible=True)"""


window.close()