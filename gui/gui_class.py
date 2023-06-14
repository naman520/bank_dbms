import PySimpleGUI as sg
import mysql.connector as sql

class GUI:
    def __init__(self):
        self.main_window=None

        self.admin_layout = [
            [sg.Text('Admin Login')],
            [sg.Text('Username: '), sg.Input(key='Username')],
            [sg.Text('Password: '), sg.Input(key='Password',password_char='*')],
            [sg.Button('Login'),sg.Button('Exit')]]

        self.account_layout =[
            [sg.Text('Account Name:')],
            [sg.Text('Account Number:'),sg.Input(key='Number')],
            [sg.Text('OTP:'),sg.Input(key='OTP')],
            [sg.Button('Login'),sg.Button('Exit')]]

        self.layout = [[sg.Text('Welcome to STATE BANK OF INDIA'),sg.Column(self.admin_layout, visible=False,key='-COL1-'), sg.Column(self.account_layout, visible=False,key='-COL2-')],
            [sg.Button('Admin'), sg.Button('Account'), sg.Button('Exit')]]

   
    def run(self):
            self.main_window = sg.Window('Introduction',self.layout,finalize=True)
    
            while True:
                #database
                conn=sql.connect(host='localhost',user='root',passwd='123456',database='BANK_DBMS')
                cur = conn.cursor()
                query = "SELECT username, passwordx FROM admin"
                cur.execute(query)
                results = cur.fetchall()

                #gui window
                event, values = self.main_window.read()
                print(event, values)
                if event in (None, 'Exit'):
                    break
                
                if event == 'Admin':
                    self.main_window['-COL1-'].update(visible=True)
                    if event in (None, 'Exit'):
                        break
                    elif event == 'Login':
                        self.username = str(values['-USERNAME-'])
                        self.password = str(values['-PASSWORD-'])
                        authenticated = False  # Initialize the variable here
                        for row in results:
                            username = row[0]
                            passwordx = row[1]
                    # Add your authentication logic here
                            if username == self.username and passwordx == self.password:
                                authenticated = True
                            break
                    if authenticated:
                        sg.popup('Login Successful!')
                    else:
                        sg.popup('Invalid Credentials!')

                
                elif event == 'Account':
                    self.main_window['-COL2-'].update(visible=True)
                    if event in (None, 'Exit'):
                        break
                    elif event == 'Login':
                        self.Account_Number = str(values['-Account Number-'])
                        self.OTP = str(values['-OTP-'])
                    # Add your authentication logic here
                        if self.Account_Number == 'admin' and self.OTP == 'admin':
                            sg.popup('Login Successful!')
                        else:
                            sg.popup('Invalid Credentials!')
            self.main_window.close()


if __name__ == '__main__':
    gui = GUI()
    gui.run()