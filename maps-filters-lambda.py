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

def square(num):
    return num**2


my_nums = [1,2,3,4,5]

for item in map(square,my_nums):
    print(item)

list(map(square,my_nums))





# +
def splicer(mystring):
    if len(mystring)%2 == 0:
        return 'EVEN'
    else:
        return mystring[0]
    
#returns word EVEN if the name has an even number of letters
#otherwise returns the first letter of the name given


# -

names = ['Andy','Eve','Sally']

list(map(splicer,names))


def check_even(num):
    return num%2==0


mynums = [1,2,3,4,5,6]

list(filter(check_even,mynums))

# +
#or
# -

for n in filter(check_even,mynums):
    print(n)







def square(num):
    result = num ** 2
    return result


square(3)


def square(num):
    return num ** 2


def square(num): return num ** 2


lambda num: num ** 2

square = lambda num: num ** 2

list(map(lambda num:num**2,mynums))


def check_even(num):
    return num%2 == 0


list(filter(lambda num:num%2 == 0, mynums))

names

list(map(lambda name:name[0],names))

list(map(lambda x:x[::-1],names))


