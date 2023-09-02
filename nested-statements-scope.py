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

# +
x = 25

def printer():
    x = 50
    return x


# -

print(x)

print(printer())

# LEGB rule format – the order python looks for functions
# -	L : Local = names assigned in any way within a function (def or lambda) and not declared global in that function
# -	E : Enclosing function locals – names in the local scope of any and all enclosing functions (def or lambda), from inner to outer
# -	G : Global (module) – names assigned at the top level of a module file, or declared global in a def within the file
# -	B : Built-in (Python) – names preassigned in the built in names module – open, range, syntax error
#

# +
# local - lambda num:num**2

# +
name = 'This is a global string'

def greet():
    #enclosing variable
    name = 'Sammy'
    
    def hello():
        #local variable
        name = "I'm a local"
        print('Hello '+name)
        
    hello()
    
greet()

# +
#global variable
name = 'This is a global string'

def greet():
    
    # name = 'Sammy'
    
    def hello():
        print('Hello '+name)
        
    hello()
    
greet()
# -

help(len)

# +
x = 50 

def func(x):
    print(f'x is {x}')
    
    #local reassignment 
    x = 200 
    print(f'i just locally changed x to {x}')


# -

func(x)

print(x)

# the reassignment of x ONLY happens in the local reassignment of x hence why you can still print(x) as 50 - the global x

# What if you wanted to actually change global x within this function: 

# +
x = 50 

def func():
    #declare global x - jump to global level and grab global x 
    # this means anything that happens will happen to global 
    global x 
    print(f'x is {x}')
    
    #local reassignment 
    #local reassignment will now effect the global x
    x = 'NEW VALUE' 
    print(f'i just locally changed global x to {x}')


# -

print(x) #function not yet executed

func()

print(x)

# Alternate way of doing this - and generally maybe the safer way to do this, is to reassign x via:

# +
x = 50

def func(x):
    print(f'x is {x}')
    
    x = 'NEW VALUE' 
    print(f'i just locally changed x to {x}')
    return x


# -

print(x)

x = func(x)

print(x)


