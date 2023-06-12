import PySimpleGUI as sg

def login_window():
    layout = [
        [sg.Text('Admin Login')],
        [sg.Text('Username:'), sg.Input(key='-USERNAME-')],
        [sg.Text('Password:'), sg.Input(key='-PASSWORD-', password_char='*')],
        [sg.Button('Login'), sg.Button('Cancel')]
    ]

    return sg.Window('Login', layout, finalize=True)

#def customer():

def main_window():
    layout = [
        [sg.Button('ADMIN'), sg.Button('ACCOUNT HOLDER')]
    ]

    return sg.Window('BANK DBMS', layout, finalize=True)

# Create the windows
login_window = login_window()
main_window = main_window()

# Display and interact with the Main Window
while True:
    window, event, values = sg.read_all_windows()

    if window == main_window and event == sg.WINDOW_CLOSED:
        break

    if window == main_window and event == 'ADMIN':
        login_window = login_window()

    if window == login_window and event == sg.WINDOW_CLOSED or event == 'Cancel':
        login_window.close()

    if window == login_window and event == 'Login':
        username = values['-USERNAME-']
        password = values['-PASSWORD-']
        
        # Add your authentication logic here
        if username == 'admin' and password == 'admin':
            sg.popup('Login Successful!')
        else:
            sg.popup('Invalid Credentials!')

        # Close the login window after login attempt
        login_window.close()

# Close all windows at the end
main_window.close()