import PySimpleGUI as sg

admin_layout = [
    [sg.Text('Admin Login')],
    [sg.Text('Username: '), sg.Input(key='Username')],
    [sg.Text('Password: '), sg.Input(key='Password',password_char='*')],
    [sg.Button('Login'),sg.Button('Exit')]    
] 

account_layout =[
    [sg.Text('Account Name:')],
    [sg.Text('Account Number:'),sg.Input(key='Number')],
    [sg.Text('OTP:'),sg.Input(key='OTP')],
    [sg.Button('Login'),sg.Button('Exit')]
]

defaultx = [
    [sg.Text('Welcome to STATE BANK OF INDIA')],
    
]

layout = [[sg.Column(defaultx,key='-COL1-'),sg.Column(admin_layout, visible=False,key='-COL2-'), sg.Column(account_layout, visible=False,key='-COL3-')],
        [sg.Button('Admin'), sg.Button('Account'), sg.Button('Exit')]
]



main_window = sg.Window('Introduction',layout,finalize=True)
while True:
    event, values = main_window.read()
    print(event, values)
    if event in (None, 'Exit'):
        main_window.close()
        
    if event == 'Admin':
        main_window['-COL2-'].update(visible=True)
        if event in (None, 'Exit'):
            main_window.close()
        elif event == 'Login':
            username = str(values['-USERNAME-'])
            password = str(values['-PASSWORD-'])
        # Add your authentication logic here
            if username == 'admin' and password == 'admin':
                sg.popup('Login Successful!')
            else:
                sg.popup('Invalid Credentials!')
        
    elif event == 'Account':
        main_window['-COL3-'].update(visible=True)
        if event in (None, 'Exit'):
            main_window.close()
        elif event == 'Login':
            Account_Number = str(values['-Account Number-'])
            OTP = str(values['-OTP-'])
        # Add your authentication logic here
            if Account_Number == 'admin' and OTP == 'admin':
                sg.popup('Login Successful!')
            else:
                sg.popup('Invalid Credentials!')
main_window.close()