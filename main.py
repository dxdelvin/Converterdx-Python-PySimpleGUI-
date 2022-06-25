import PySimpleGUI as sg

layout = [
    [sg.DropDown(["Km to M", "Hour to Minute", "Kg to mg", "TIME(COMING SOON)"], key="-UNIT-", size=(30, 8))],
    [sg.InputText(size=(15, 8), key="-TOP_TEXT-"), sg.Button('Convert', key="-TOP_BTN-")],
    [sg.HorizontalSeparator()],
    [sg.InputText(size=(15, 8), key="-BOTTOM_TEXT-"), sg.Button('Convert', key="-BOTTOM_BTN-")],
    [sg.Text("",key="-TEXT-")]
]


def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


window = sg.Window('Converter', layout, element_justification='c')

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break

    if event == "-TOP_BTN-":
        input_value = values["-TOP_TEXT-"]
        if isfloat(input_value):
            match values["-UNIT-"]:
                case "Km to M":
                    output_value = round(float(input_value), 2) * 1000
                    window["-TEXT-"].update(f"{input_value}km is equal to {output_value}m")
                case "Hour to Minute":
                    output_value = round(float(input_value), 2) * 60
                    window["-TEXT-"].update(f"{input_value}hr is equal to {output_value}min")
                case "Kg to mg":
                    output_value = round(float(input_value), 2) * 1000
                    window["-TEXT-"].update(f"{input_value}kg is equal to {output_value}g")
            window["-BOTTOM_TEXT-"].update(output_value)
        else:
            window["-TEXT-"].update("Please Enter a Number")

    elif event == "-BOTTOM_BTN-":
        input_value = values["-BOTTOM_TEXT-"]
        if isfloat(input_value):
            match values["-UNIT-"]:
                case "Km to M":
                    output_value = round(float(input_value), 2) / 1000
                    window["-TEXT-"].update(f"{input_value}m is equal to {output_value}km")
                case "Hour to Minute":
                    output_value = round(float(input_value), 2) / 60
                    window["-TEXT-"].update(f"{input_value}min is equal to {output_value}hr")
                case "Kg to mg":
                    output_value = round(float(input_value), 2) / 1000
                    window["-TEXT-"].update(f"{input_value}g is equal to {output_value}kg")

            window["-TOP_TEXT-"].update(output_value)
        else:
            window["-TEXT-"].update("Please Enter a Number")
window.close()
