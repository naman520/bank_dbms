import PySimpleGUI as sg
import mysql.connector as sql

sg.theme('DarkAmber')  # Add a touch of color
# All the stuff inside your window.
layout = [[sg.Text('Select'), sg.InputText()],
          [sg.Text('Password'), sg.InputText(password_char='*')],
          [sg.Button('Login'), sg.Button('Cancel')]]
