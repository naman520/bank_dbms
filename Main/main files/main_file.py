import PySimpleGUI as sg
import final_admin , final_account

sg.theme('DarkAmber')
# All the stuff inside your window.
layout_main_window = [[sg.Image('Untitledlogo.png',expand_x=True, expand_y=True )],
            [sg.Button('Admin'),sg.Button('Customer'),sg.Button('Cancel'),sg.Button('XY')]]

window = sg.Window('Python Bank Of INDIA', layout_main_window)

while True:
   event, values = window.read()
   print(event, values)
   if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
      break
   if event == 'Admin':
      final_admin.main_window()
   elif event == 'Customer':
      final_account.customer()
   elif event == 'XY':
      sg.popup_auto_close('Welcome To Python Bank Of INDIA',sg.Image('Untitledlogo.png',expand_x=True, expand_y=True ))

window.close()