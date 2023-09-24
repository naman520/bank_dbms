import PySimpleGUI as sg

layout = [[sg.Frame("PASTA", layout=[
    [sg.Text("Italian Style: "), sg.Push(), sg.Text("500")],
    [sg.Text("Indian Style: "), sg.Push(), sg.Text("300")],
    [sg.Text("American Style: "), sg.Push(), sg.Text("1000")],
    [sg.Button("Click me !", s=(20,10))]
],size=(200,100))]]

layout_2 = [[sg.Frame("PIZZA", layout=[
    [sg.Text("Italian Style: "), sg.Push(), sg.Text("200")],
    [sg.Text("Indian Style: "), sg.Push(), sg.Text("1000")],
    [sg.Text("American Style: "), sg.Push(), sg.Text("300")],
    [sg.Button("Click me !")]
],size=(200,100))]]


window = sg.Window('Pasta Shop', layout ,resizable=True)


while True:
    event, values = window.read()
    print(event, values)

    if event == sg.WIN_CLOSED:
        break

    if event == "-ChangeLayout-":
        layout = layout_2
