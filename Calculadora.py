# Import Module
from PySimpleGUI import *
import PySimpleGUI as sg

# GUI Layout
layout = [[Txt('' * 10)],
		[Text('', size = (15, 1), font = ('Helvetica', 18),
				text_color = 'black', key = 'input')],
		[Txt('' * 10)],
		[ReadFormButton('c'), ReadFormButton('«')],
		[ReadFormButton('7'), ReadFormButton('8'), ReadFormButton('9'), ReadFormButton('/')],
		[ReadFormButton('4'), ReadFormButton('5'), ReadFormButton('6'), ReadFormButton('*')],
		[ReadFormButton('1'), ReadFormButton('2'), ReadFormButton('3'), ReadFormButton('-')],
		[ReadFormButton('.'), ReadFormButton('0'), ReadFormButton('='), ReadFormButton('+')],
		]

# Set PySimpleGUI
form = FlexForm('CALCULATOR', default_button_element_size = (5, 2),
				auto_size_buttons = False, grab_anywhere = False)
form.Layout(layout)

# Result Value
Result = ''

# Make Infinite Loop
while True:
	# Button Values
	button, value = form.Read()
	
	# Check Press Button Values
	if button == 'c':
		Result = ''
		form.FindElement('input').Update(Result)
	elif button=='«':
		Result = Result[:-1]
		form.FindElement('input').Update(Result)
	elif len(Result) == 16 :
		pass
	
# Results
	elif button == '=':
		Answer = eval(Result)
		Answer = str(round(float(Answer),3))
		form.FindElement('input').Update(Answer)
		Result = Answer
		
	# close the window
	elif button == 'Quit' or button == None:
		break
	else:
		Result += button
		form.FindElement('input').Update(Result)
	if Result == "10.0":
		print("Bienvenido")
		sg.Popup("Bienvenido", keep_on_top=True)
