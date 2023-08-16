import PySimpleGUI as sg
import final_admin
sg.theme('DarkAmber')  # Add a touch of color
# All the stuff inside your window.
layout_1 = [[sg.Image('Untitledlogo.png',expand_x=True, expand_y=True )],
            [sg.Button('Admin'),sg.Button('Customer'),sg.Button('Cancel')]]

window = sg.Window('HelloWorld', layout_1,  keep_on_top=True)
def admin():
   final_admin.adminn()

while True:
   event, values = window.read()
   print(event, values)
   if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
      break
   if event == 'Admin':
      admin()
window.close()