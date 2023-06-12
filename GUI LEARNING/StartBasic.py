# #NOTE::Single use with pop return
# import PySimpleGUI as sg      

# layout = [[sg.Text('My one-shot window.')],      
#                  [sg.InputText(key='-IN-')],
#                  [sg.InputText(key='-IN1-')],        
#                  [sg.Submit(), sg.Cancel()]]      

# window = sg.Window('Window Title', layout)    

# event, values = window.read()    
# window.close()

# text_input = values['-IN-'] + "\n" +values['-IN1-']   
# sg.popup('You entered', text_input)

# #NOTE::Single use
# import PySimpleGUI as sg

# event, values = sg.Window('Login Window',
#                   [[sg.T('Enter your Login ID'), sg.In(key='-ID-')],
#                   [sg.B('OK'), sg.B('Cancel') ]]).read(close=True)

# login_id = values['-ID-']

# #NOTE::Constant window
# import PySimpleGUI as sg      

# sg.theme('DarkAmber')    #  NOTE:: Keep things interesting for your users

# layout = [[sg.Text('Persistent window')],      
#           [sg.Input(key='-IN-')],      
#           [sg.Button('Read',size=(15,2)), sg.Exit()]]      

# window = sg.Window('Window that stays open', layout)      

# while True:                             # The Event Loop
#     event, values = window.read() 
#     print(event, values)       
#     if event == sg.WIN_CLOSED or event == 'Exit':
#         break      

# window.close()

import PySimpleGUI as sg

sg.theme('BluePurple')

layout = [[sg.Text('Your typed chars appear here:'), sg.Text(size=(10,1), key='-OUTPUT-', pad=20, relief='raised', border_width=20, background_color="red", text_color="white")],
          [sg.Input('asdf', key='-IN-')],
          [sg.FileBrowse('Browse', target='-IN-')],
          [sg.Button('Show'), sg.Button('Exit')]]

window = sg.Window('Pattern 2B', layout)


while True:  # Event Loop
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Show':
        # Update the "output" text element to be the value of "input" element
        window['-OUTPUT-'].update(values['-IN-'])

window.close()