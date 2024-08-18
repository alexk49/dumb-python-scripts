'''
Potential methods include:

Gregory-Leibniz series 
 pi = 4*(1 - 1/3 + 1/5 - 1/7 + ... 

Nilakantha series
	π=3+4/(2·3·4)-4/(4·5·6)+4/(6·7·8)-4/(8·9·10)+4/(10·11·12)-4/(12·13·14) ⋯


formula to calculate pi: 
x * sin(180 / x). For this to work, make sure your calculator is set to Degrees. The reason this is called a Limit is because the result of it is 'limited' to pi. As you increase your number x, the result will get closer and closer to the value of pi. 

'''
import math


def how_many_decimals():
	user_input = ''
	while user_input.isdigit() == False:
		user_input = input("How many decimals would you like pi to have?\n")
	if user_input.isdigit():
		user_input = int(user_input)
		return user_input

def print_setup(decimals,method):
	decimals = str(decimals)
	print("Oh, okay, we'll find pi to {} decimal places, and we're going to use the {} method".format(decimals,method))


def series_limit():
	series_limit = ''
	while series_limit.isdigit() == False:
		series_limit = input(("How far would you like to go in the series?\nThe higher your choice the more accurate we'll be\nDon't get too carried away though, we haven't got all day\n"))
	if series_limit.isdigit():
		return int(series_limit)

def gregory_leibniz_series(series_limit):
	total = 0.0
	term = 1.0
	for i in range (1,series_limit+1):
		denom = 2*i-1
		total += term/denom
		term = -term
	pi = 4*total
	return pi
		
def nilakantha_series(series_limit):
	pi = 3
	sign = 1
	n = 2
	for x in range(series_limit+1):
	    pi = pi + (sign*(4/((n)*(n+1)*(n+2))))
	    #for addition and subtraction of alternate terms
	    sign = sign*(-1)
	    #Increment by 2 according to formula
	    n = n + 2
	return pi

method = input("How would you like me to find pi?\nCheat method?\nGregory-Leibniz series?\nNilakantha?\n")

if method[0].lower() == 'c':
	print("Okay, we'll cheat!")
	decimals = how_many_decimals()
	
	print_setup(decimals,method)

	print("Here you go:")
	print(round(math.pi,decimals))

if method[0].lower() == 'g':
	print("Okay, we'll use the Gregory-Leibniz series... This can take a while...")

	decimals = how_many_decimals()
	print_setup(decimals,method)

	limit = series_limit()

	gl_pi = gregory_leibniz_series(limit)

	print("Here you go:")
	print(round(gl_pi,decimals))

if method[0].lower() == 'n':
	print("Okay, we'll use the Nilakantha series... This can take a while...")

	decimals = how_many_decimals()
	print_setup(decimals,method)

	limit = series_limit()

	nil_series = nilakantha_series(limit)

	print("Here you go:")
	print(round(nil_series,decimals))
