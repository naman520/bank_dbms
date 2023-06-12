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

def main_window():
    layout = [
        [sg.Button('ADMIN'), sg.Button('ACCOUNT HOLDER')]
    ]

    return sg.Window('BANK DBMS', layout, finalize=True)

# Create the windows
login_window = login_window()
customer = customer()
main_window = main_window()

# Display and interact with the Main Window
while True:
    window, event, values = sg.read_all_windows()
    print(window, event, values)
    if window == main_window and event == sg.WINDOW_CLOSED:
        break

    if window == main_window and event == 'ADMIN' or 'ACCOUNT HOLDER':
        if event == 'ADMIN':
            login_window = login_window()
        if event == 'ACCOUNT HOLDER':
            customer = customer()

    if window == login_window or customer and event == sg.WINDOW_CLOSED or event == 'Cancel':
        login_window.close(),customer.close()


#   BUG:: RUNNING TWO SEPERATE CONDITONS TOGETHER
#           FIX::       create seperate if statements for login and customers 
#           ERROR::     variables like _NUMBER are not filled but are called in combined if statements of login and customer
    if window == login_window or customer and event == 'Login':
        username ,number = values['-USERNAME-'] ,values['-NUMBER-']
        password ,otp = values['-PASSWORD-'], values['-OTP-']
        
        # Add your authentication logic here
        if username == 'admin' and password == 'admin':
            sg.popup('Login Successful!')
        else:
            sg.popup('Invalid Credentials!')

        # Close the login window after login attempt
        login_window.close()

    

# Close all windows at the end
main_window.close()