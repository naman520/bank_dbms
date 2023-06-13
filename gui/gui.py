import PySimpleGUI as sg


# NOTE ::: Use class ::  class login_window(sg.Window):
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
main_window = main_window()

# Display and interact with the Main Window
while True:
    window, event, values = sg.read_all_windows()
    print(window, event, values)
    # ADMIN LOGIN CODE
    if window == main_window and event == sg.WINDOW_CLOSED:
        break

    if window == main_window and event == 'ADMIN':
        if event == 'ADMIN':
            login_window = login_window()

    if window == login_window and event == sg.WINDOW_CLOSED or event == 'Cancel':
        login_window.close()

    if window == login_window and event == 'Login':
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
    if window == main_window and event == sg.WINDOW_CLOSED:
        break

    if window == main_window and event == 'ACCOUNT HOLDER':
        if event == 'ACCOUNT HOLDER':
            customer = customer()

    if window == customer and event == sg.WINDOW_CLOSED or event == 'Cancel':
        customer.close()

    if window == customer and event == 'Login':
        number = values['-NUMBER-'] 
        otp = values['-OTP-']
        
        # Add your authentication logic here
        if number == 'admin' and otp == 'admin':
            sg.popup('Login Successful!')
        else:
            sg.popup('Invalid Credentials!')

        # Close the login window after login attempt
        customer.close()

    

# Close all windows at the end
main_window.close()