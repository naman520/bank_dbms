import mysql.connector as db
import matplotlib.pyplot as plt
import warnings , PySimpleGUI as sg
warnings.filterwarnings('ignore')

sg.theme('DarkTeal12')
conn = db.connect(host='localhost', user='root', passwd='123456', database='BANK_DBMS')
cur = conn.cursor()

layout = [[sg.Button('Exit'),sg.Button('Analysis')]]
window = sg.Window('Analysis Window',layout)
while True:
    event,values = window.read()
    if  event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event=='Analysis':
        # x axis values
        x = [1, 2, 3]
        # corresponding y axis values
        y = [2, 4, 1]

        # plotting the points
        plt.plot(x, y)

        # naming the x axis
        plt.xlabel('x - axis')
        # naming the y axis
        plt.ylabel('y - axis')

        # giving a title to my graph
        plt.title('My first graph!')

        # function to show the plot
        plt.show()
        sg.popup_auto_close('This Graph is only for example',auto_close_duration=20)

window.close()

# q2=pd.read_sql_query('''select * from customer_details''',conn)
# q2.to_csv('file2.csv',index=False)
# print("ok")