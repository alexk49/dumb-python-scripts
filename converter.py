import PySimpleGUI as sg

layout = [
		[sg.Input(key = '-INPUT-'),
		sg.Spin(['km to miles','kg to pounds'],key='-UNIT-'),
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

	if event == '-CONVERT-' and values['-UNIT-'] == 'km to miles':
		print(values)
		km_value = int(values['-INPUT-'])
		miles_value = km_value*0.6214
		window['-OUTPUT-'].update(round(miles_value,2))

	if event == '-CONVERT-' and values['-UNIT-'] == 'kg to pounds':
		kg_value = int(values['-INPUT-'])
		pounds_value = kg_value*2.2046
		window['-OUTPUT-'].update(round(pounds_value,2))

window.close()
