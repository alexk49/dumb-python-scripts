# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.13.8
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

def say_hello():
    print('hello')
    print('how are you')


say_hello()

say_hello


def say_hello(name='Whatever'):
    print(f'hello {name}')


say_hello('bear')

say_hello()


def add_num(num1,num2):
    return num1+num2


add_num(10,20)

result = add_num(1,20)

result


def print_result(a,b):
    print(a+b)


def return_result(a,b):
    return a+b


print_result(10,20)

result = print_result(10,20)

result

return_result(10,20)

result = return_result(10,20)

result


def myfunc(a,b):
    print(a+b)
    return a+b


result = myfunc(10,20)

result


def sum_numbers(num1,num2):
    return num1+num2


sum_numbers(10,20)

sum_numbers('10','20')

sum_numbers('a','b')


