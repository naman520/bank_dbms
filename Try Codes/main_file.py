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
            #[sg.Text(':'),sg.Input(key='OTP')], to be decided
            [sg.Button('Login'),sg.Button('Exit')]]

        self.layout = [[sg.Text('Welcome to STATE BANK OF INDIA'),sg.Column(self.admin_layout, visible=False,key='-COL1-'), sg.Column(self.account_layout, visible=False,key='-COL2-')],
            [sg.Button('Admin'), sg.Button('Account'), sg.Button('Exit')]]

   
    def run(self):
            self.main_window = sg.Window('Introduction',self.layout,finalize=False)
    
            while True:
                #database
                conn=sql.connect(host='localhost',user='root',passwd='123456',database='BANK_DBMS')
                cur = conn.cursor()
                query = "SELECT * FROM admin"
                q2 = "SELECT acc_no FROM user "
                cur.execute(query)
                results = cur.fetchall()
                cur.execute(q2)
                r2 = cur.fetchall()

                #gui window
                event, values = self.main_window.read()
                print(event, values)
                if event in (None, 'Exit'):
                    break
                
                if event == 'Admin':
                    self.main_window['-COL1-'].update(visible=True)
                    if event in (None, 'Exit'):
                        event = sg.WIN_CLOSED
                        break
                    elif event == 'Login':
                        if (values[0],values[1])in results:
                            print("WELCOME !!! ",values[0])
                        else:
                            print("UNAUTHORISED LOGIN !!!")
                            event = sg.WIN_CLOSE_ATTEMPTED_EVENT
                            break

                
                elif event == 'Account':
                    self.main_window['-COL2-'].update(visible=True)
                    if event in (None, 'Exit'):
                        break
                    elif event == 'Login':
                    # Add your authentication logic here
                        if (values[0]) in r2:
                            sg.popup('Login Successful!')
                        else:
                            sg.popup('Invalid Credentials!')
                            event = sg.WIN_CLOSE_ATTEMPTED_EVENT
                            break
            self.main_window.close()


if __name__ == '__main__':
    gui = GUI()
    gui.run()