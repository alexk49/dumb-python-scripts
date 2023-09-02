import PySimpleGUI as sg

# takes two arguments, title and layout

# this will create 3 elements 
layout = [
			[sg.Text("Text",enable_events = True,key = '-TEXT-'),sg.Spin(['item 1','item 2'])],
			[sg.Button('Button',key="-BUTTON1-")],
			[sg.Input(key = '-INPUT-')],
			[sg.Text("Hello"),sg.Button("Goodbye",key="-BUTTON2-")]
 ]

window = sg.Window('Converter',layout)

while True:
	# read returns an event and value
	event,values = window.read()

	if event == sg.WIN_CLOSED:
		break

	if event == '-BUTTON1-':
		window['-TEXT-'].update(values['-INPUT-'])

	if event == '-BUTTON2-':
		print("Goodbye")
		break

	if event == "-TEXT-":
		print("text was pressed")

window.close()