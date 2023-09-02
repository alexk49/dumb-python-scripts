import PySimpleGUI as sg

layout = [
		[sg.Input(key = '-INPUT-'),
		sg.Spin(['km to miles','kg to pounds'],key='-UNITS-'),
		sg.Button('Convert',key='-CONVERT-')
		],
		[sg.Text("Output",key='-OUTPUT-')],
		]

window = sg.Window('Converter',layout)

while True:
	# read returns an event and value
	event,values = window.read()

	if event == sg.WIN_CLOSED:
		break

	if event == '-CONVERT-':
		input_value = values['-INPUT-']
		if input_value.isnumeric():
			if values['-UNITS-'] == 'km to mile':
					output = round(float(input_value) * 0.6214,2)
					output_string = f"{input_value} km are {output} miles."

					window['-OUTPUT-'].update(output_string)
			if values['-UNITS-'] == 'kg to pounds':
					output = round(float(input_value) * 2.20462,2)
					output_string = f'{input_value} kg are {output} pounds.'

					window['-OUTPUT-'].update(output_string)
		else:
			window['-OUTPUT-'].update("Please enter a number")

window.close()

'''
look up match values and case which didn't work for some reason
'''