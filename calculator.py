# Needs More Changes to User's Mistake Handling Part, Other Hand Works Perfectly Fine



import PySimpleGUI as sg


def create_window(theme):
    sg.theme(theme)
    sg.set_options(font="Lato, 16", button_element_size=[6, 3])
    layout = [
        [sg.Text('Start Calculating ', font="Arial_Black 24", justification="r", expand_x=True, key="-TEXT-",pad=(10, 20),
                 right_click_menu=theme_menu),],

        [sg.Button("Clear(C)", expand_x=True), sg.Button("Enter(=)", expand_x=True), sg.Button("Backspace")],
        [sg.Button("7", size=(6, 3)), sg.Button("8", size=(6, 3)), sg.Button("9", size=(6, 3)),
         sg.Button("X", key="*", size=(6, 3))],
        [sg.Button("4", size=(6, 3)), sg.Button("5", size=(6, 3)), sg.Button("6", size=(6, 3)),
         sg.Button("-", size=(6, 3))],
        [sg.Button("1", size=(6, 3)), sg.Button("2", size=(6, 3)), sg.Button("3", size=(6, 3)),
         sg.Button("+", size=(6, 3))],
        [sg.Button("0", expand_x=True), sg.Button(".", size=(6, 3)), sg.Button("/", size=(6, 3))],
        [],
    ]

    return sg.Window("Calculator", layout)


theme_menu = ['menu', ['DarkGrey6', 'LightGrey5', 'LightBrown10', 'Default1', 'Random']]
window = create_window("LightGrey1")

current_num = []
operation = []
symbols = ["*", "+", "-", "/"]
num = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event in theme_menu[1]:
        window.close()
        window = create_window(event)

    if event in num:
        current_num.append(event)
        current_string = ''.join(current_num)
        window['-TEXT-'].update(current_string)

    if event in symbols:
        operation.append("".join(current_num))
        current_num = []
        operation.append(event)
        window["-TEXT-"].update("")
        window["-TEXT-"].update(event)
        print(operation)

    if event == "Backspace":
        if operation != [] and current_num == []:
            print(operation)
            operation.pop()
            current_string = ''.join("")
            window["-TEXT-"].update(current_string)

        else:
            current_num.pop()
            current_string = ''.join(current_num)
            window["-TEXT-"].update(current_string)


    if event == 'Enter(=)':
        operation.append(''.join(current_num))
        result = eval(''.join(operation))
        # print("".join(operation))
        operation = []
        current_num.pop()
        current_num.append(str(result))
        # print(current_num)
        window["-TEXT-"].update(result)


    if event == 'Clear(C)':
        current_num = []
        operation = []
        window["-TEXT-"].update("")

window.close()
